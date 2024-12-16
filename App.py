import streamlit as st 

st.title(":orange[Chatbot & Language Translation App using Groq and Llama 3.3 Versatile]")

# Introduction to the Chatbot & Language Translation App

st.markdown(
    """
    **👋 Meet Your AI Assistant:** A state-of-the-art application combining two powerful AI functionalities:

    1. 🤖 **Chatbot**: An intelligent conversational agent powered by Groq and Meta's Llama-3.3-70b-Versatile model. It delivers accurate, contextual responses to your queries.
    2. 🌍 **Language Translation**: Translate text effortlessly into multiple languages using cutting-edge AI technology. Perfect for breaking language barriers.
    
    ---
    
    ### 🚀 Key Features
    - **Dynamic Conversations**: Engage in meaningful discussions with the AI-powered chatbot.
    - **Multi-Language Support**: Translate text into Hindi, Telugu, Kannada, Tamil, Malayalam, Marathi, French, Spanish, Japanese, and Simplified Chinese.
    - **Easy-to-Use Interface**: Intuitive design for users of all technical backgrounds.

    Ready to explore? Let’s dive in! 🧭
    """
)

# Expandable sections for additional interactivity
with st.expander("🔍 What is Groq?", expanded=True):
    st.markdown(
        """
        Groq is a leading innovator in artificial intelligence and machine learning technologies, delivering advanced solutions for AI workloads.
        
        **Key Highlights:**
        - **AI Models**: Cutting-edge models for chatbots, translation, and more.
        - **Hardware Acceleration**: Optimized hardware for faster AI processing.
        - **Developer Tools**: APIs and frameworks for seamless integration.
        - **Efficiency Focused**: Reduced resource consumption for greater cost-effectiveness.
        
        Learn more about how Groq empowers AI applications to achieve top performance!🌟
        """
    )

with st.expander("🧠 What is Llama 3.3-70b-Versatile?", expanded=True):
    st.markdown(
        """
        Meta’s Llama 3.3-70b-Versatile is a cutting-edge large language model designed to excel in:
        
        - **Instruction Following**: Excels at reasoning and task execution.
        - **Multilingual Processing**: Seamlessly handles diverse languages.
        - **Cost-Effectiveness**: Up to 80% reduction in ownership costs compared to previous models.
        - **High-Quality Outputs**: Delivers precision in coding, math, and natural language tasks.

        With optimized architecture and unparalleled performance, Llama 3.3 redefines AI capabilities!🌟
        """
    )

# Call to Action
st.markdown(
    """
    ### 💡 Explore the Application:
    - 🔗 **Chatbot**: Navigate to the Chatbot page to start a conversation.
    - 🌐 **Language Translation**: Translate your text seamlessly across multiple languages.

    🚀 **Let’s transform the way you interact with AI!**
    """
)
