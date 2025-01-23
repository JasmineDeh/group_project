import streamlit as st 

# Page and side bar title.
st.markdown("# The Basics of Machine Learning")
st.sidebar.markdown("# Content Menu")


# Side bar menu to add links.
st.sidebar.markdown("***Section One: Supervised Learning.***")
st.sidebar.markdown("***Section Two: Unsupervised Learning.***")
st.sidebar.markdown("***Section Three: Neural Networks.***")
st.sidebar.markdown("***Section Four: Python Implementation.***")


# Subtitle for brief intro to machine learning.
st.markdown("**Welcome to a beginners guide to Machine Learning techniques and their applications!**")

# Brief intro paragraph.
st.markdown("Machine learning has become an integral part of solving real-world problems, making significant strides across diverse domains like healthcare, finance, transportation, and entertainments. This web app is designed to serve as an accessible guide for beginners, helping you understand an apply key machine learning techniques to real-world datasets.")


# Following intro paragraph (draws attention to real-world applications).
st.markdown("Whether you’re curious about how Netflix recommends your favourite shows or how self-driving cars navigate roads, this app will provide the foundational knowledge you need to explore there innovations further.")


# Introduction to content.
# Add slider to show how ML techniques work e.g. for linear regression show how changing the slope or intercept affects a line of best fit on a graph.
st.markdown("**What will you learn?**")
st.markdown("This web app is structured into several sections, each focusing on essential machine learning concepts.")
st.markdown("***Section One***: *Supervised Learning:*")
st.markdown("- Linear regression: Predict continuous outcomes like housing prices or stock market trends.")
st.markdown("-	Classification: Categorise data, such as spam email detection or predicting customer churn.")
st.markdown("***Section Two***: *Unsupervised Learning:*")
st.markdown("-	Clustering: Group similar data points, such as a customer segmentation or image compression.")
st.markdown("-	Principle component analysis (PCA): Reduce the dimensionality of datasets, helping visualise and analyse complex data efficiently.")
st.markdown("***Section Three***: *Neural Networks:*")
st.markdown("-	Understand the building blocks of artificial intelligence and how they power applications like fraud detection, speech recognition, and personalised recommendations.")
st.markdown("***Section Four***: *Virtual Reality (VR) Convolutional Neural Networks:*")
st.markdown("-	Visualise CNNs and their functions in 3D space.")
st.markdown("***Section Five***: *Python Implementation:*")
st.markdown("-	This section goes deeper into the principles and theory of each method.")
st.markdown("- Learn Learn how to implement each method in Python with statis code examples, catering to more advanced learners who want hands-on experience with the tools and techniques.")


# Connecting machine learning to real world examples.
# Add dropdown/selectbox to let users select a real-world application, display short description or visual of how ML is used in that field.
st.markdown("**How is Machine Learning applied in the real-world?**")
st.markdown("Machine learning is transforming industries and reshaping how we interact with technology, for instance:")
st.markdown("- Healthcare: Diagnosing diseases, analysing medical images, and predicting patient outcomes.")
st.markdown("-	Finance: Fraud detection, algorithmic trading, route optimisation, and predictive maintenance.")
st.markdown("-	Transportation: Autonomous vehicles, route optimisation, and predictive maintenance.")
st.markdown("-	Entertainment: Content recommendation systems, generative art, and virtual reality.")


# Demystifying machine learning terms.
st.markdown("**What's the difference between AI, ML, Deep Learning, and Generative AI?**")
st.markdown("-	Artificial Intelligence (AI): The broad field of creating systems capable of intelligent behaviour, from playing chess to making medical diagnoses.")
st.markdown("-	Machine Learning (ML): A subset of AI focused on developing algorithms that enable computers to learn patterns from data and make predictions.")
st.markdown("-	Deep Learning: A specialised branch of ML that uses neural networks with many layers to solve complex problems like image and speech recognition.")
st.markdown("-	Generative AI: A type of AI focused on generating new data, such as text, images, or audio, based on training examples, such as ChatGPT or DALL-E.")


# Brief insight into AI.
# Use expander to let users click to reveal more about the history of evolution of AI/ML. 
# Or use button and plot to let users click a button to generate a word cloud for key ML terms.
st.markdown("**Why is AI so important?**")
st.markdown("AI and ML are at the forefront of technological advancement, driving innovation in science and industry. From accelerating drug discovery in pharmaceuticals to improving manufacturing efficiency and developing groundbreaking technologies in renewable energy, their impact is profound and far-reaching. By gaining a foundational understanding of ML, you’ll join the growing community of individuals shaping the future of these transformative fields.")


# Quiz.
st.markdown("**Quiz time!**")
question_one = st.radio(
    "What is meant by the term Artificial Intelligence (AI)?",
    ("A system capable of intelligent behaviour.", "A type of data analysis.", "A type of electrical outlet."))
if st.checkbox("Answer 1"):
    st.write("A system capable of intelligent behaviour.")

question_two = st.radio(
    "How can machine learning algorithms benefit Healthcare?",
    ("By analysing medical images.", "By giving patients an apple a day to keep the doctor away.", "By teleporting patients running late to their appointments."))
if st.checkbox("Answer 2"):
    st.write("By analysing medical images.")

question_three = st.radio(
    "What of these machine learning techniques is linear regression?",
    ("Supervised Learning.", "Unsupervised Learning.", "Superduper Learning."))
if st.checkbox("Answer 3"):
    st.write("Supervised Learning.")


# Star rating to let users' rate how much they know about ML before starting.
knowledge_slider = st.slider("How much do you know about Machine Learning?")
st.write("About", knowledge_slider, "% confident in Machine Learning topics.")
st.write("(Keep note of me to reflect after completing the content!)")


# Progress bar to indicate the users learning journey.
st.markdown("**Get started!**")
st.markdown("Dive into the sections, experiment with datasets, and watch your skills grow as you progress through this app. Let’s demystify machine learning together and unlock its potential to address real-world challenges!")

