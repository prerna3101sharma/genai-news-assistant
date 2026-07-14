import streamlit as st

from services.news_service import NewsService
from services.summarizer import Summarizer
from services.sentiment import SentimentAnalyzer
from services.keyword import KeywordExtractor
from services.entities import EntityExtractor
from services.qa_engine import QAEngine


# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Intelligent News Assistant",
    page_icon="📰",
    layout="wide"
)

st.title("📰 Intelligent News Assistant")
st.markdown(
    "### AI Powered News Summarization, Sentiment Analysis & Question Answering"
)

st.divider()

# -------------------------------------------------
# INITIALIZE SERVICES
# -------------------------------------------------
try:
    news_service = NewsService()
    summarizer = Summarizer()
    sentiment_analyzer = SentimentAnalyzer()
    keyword_extractor = KeywordExtractor()
    entity_extractor = EntityExtractor()
    qa_engine = QAEngine()

    # st.success("✅ Services initialized")

except Exception as e:
    st.exception(e)
    st.stop()
# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------

if "articles" not in st.session_state:
    st.session_state.articles = []

if "selected_article" not in st.session_state:
    st.session_state.selected_article = None

if "summary" not in st.session_state:
    st.session_state.summary = None

if "sentiment" not in st.session_state:
    st.session_state.sentiment = None

if "keywords" not in st.session_state:
    st.session_state.keywords = None

if "entities" not in st.session_state:
    st.session_state.entities = None


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("News Search")

query = st.sidebar.text_input(
    "Enter Topic",
    placeholder="Artificial Intelligence"
)

fetch_button = st.sidebar.button("Fetch News")


# -------------------------------------------------
# FETCH NEWS
# -------------------------------------------------

if fetch_button:

    with st.spinner("Fetching latest news..."):

        try:

            articles = news_service.search_news(query)

            st.session_state.articles = articles

            st.session_state.selected_article = None
            st.session_state.summary = None
            st.session_state.sentiment = None
            st.session_state.keywords = None
            st.session_state.entities = None

            st.sidebar.success(f"{len(articles)} articles found!")

        except Exception as e:

            st.error(e)


# -------------------------------------------------
# ARTICLE SELECTION
# -------------------------------------------------

if st.session_state.articles:

    titles = [article["title"] for article in st.session_state.articles]

    selected_title = st.selectbox(
        "Select an Article",
        titles
    )

    selected_article = next(
        article
        for article in st.session_state.articles
        if article["title"] == selected_title
    )

    if (
        st.session_state.selected_article is None
        or st.session_state.selected_article["url"] != selected_article["url"]
    ):

        with st.spinner("Downloading article..."):

            st.session_state.selected_article = news_service.get_article(
                selected_article
            )

            st.session_state.summary = None
            st.session_state.sentiment = None
            st.session_state.keywords = None
            st.session_state.entities = None


# -------------------------------------------------
# DISPLAY ARTICLE
# -------------------------------------------------

if st.session_state.selected_article:

    article = st.session_state.selected_article
    # st.write(article)
    # -------------------------------------------------
    # FORMAT ARTICLE
    # -------------------------------------------------

    article_text = article["text"]

    paragraphs = article_text.split("\n")

    formatted_article = ""

    for para in paragraphs:
        if para.strip():
            formatted_article += f"""
            <p style="
                text-align: justify;
                font-size:17px;
                line-height:1.8;
                margin-bottom:18px;
            ">
            {para}
            </p>
            """


    # --------------------------------------------
    # TABS
    # --------------------------------------------

    article_col, ai_col = st.columns([2.8,1.2], gap="large")

    with article_col:

        st.header(article["title"])

        if article.get("top_image"):
            st.image(article["top_image"], use_container_width=True)

        st.caption(
            f"👤 {', '.join(article.get('authors', ['Unknown']))} | 📅 {article.get('publish_date')}"
        )

        st.divider()

        st.markdown(formatted_article, unsafe_allow_html=True)


    with ai_col:

        st.subheader("🤖 AI Assistant") 
        # --------------------------------------------
        # SUMMARY
        # --------------------------------------------

        with st.container(border=True):

            st.markdown("### 📄 Summary")

            if st.button("Generate Summary", use_container_width=True):

                with st.spinner("Generating..."):

                    st.session_state.summary = summarizer.summarize(article["text"])

            if st.session_state.summary:

                st.success(st.session_state.summary)

        # --------------------------------------------
        # SENTIMENT
        # --------------------------------------------

        with st.container(border=True):

            st.markdown("### 😊 Sentiment")

            if st.button("Analyze Sentiment", use_container_width=True):

                with st.spinner("Analyzing..."):

                    st.session_state.sentiment = sentiment_analyzer.analyze_sentiment(article["text"])

            if st.session_state.sentiment:

                st.info(st.session_state.sentiment)

        # --------------------------------------------
        # KEYWORDS
        # --------------------------------------------

        with st.container(border=True):

            st.markdown("### 🔑 Keywords")

            if st.button("Extract Keywords", use_container_width=True):

                st.session_state.keywords = keyword_extractor.extract_keywords(article["text"])

            if st.session_state.keywords:

                for keyword in st.session_state.keywords:

                    st.badge(keyword)

        # --------------------------------------------
        # ENTITIES
        # --------------------------------------------

        with st.container(border=True):

            st.markdown("### 🏷 Entities")

            if st.button("Extract Entities", use_container_width=True):

                st.session_state.entities = entity_extractor.extract_entities(article["text"])

            if st.session_state.entities:

                st.dataframe(
                    st.session_state.entities,
                    hide_index=True,
                    use_container_width=True
                )

        # --------------------------------------------
        # QA
        # --------------------------------------------

        with st.container(border=True):

            st.markdown("### 💬 Ask AI")

            question = st.text_input(
                "Ask anything about this article..."
            )

            if st.button("Ask AI", use_container_width=True):

                answer = qa_engine.answer_question(
                    article,
                    question
                )

                st.success(answer)

else:

    st.info("Search for a topic to begin.")
footer_html = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: black;
    color: white;
    text-align: center;
    padding: 10px 0;
    font-size: 14px;
    z-index: 9999;
}
</style>
<div class="footer">
    <p>Developed with ❤️ by PRERNA SHARMA</p>
</div>
"""

# Render the footer
st.markdown(footer_html, unsafe_allow_html=True)