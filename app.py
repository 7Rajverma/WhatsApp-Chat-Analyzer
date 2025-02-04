import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyzer")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)


    #fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('Notification')
    user_list.sort()
    user_list.insert(0, 'Overall')

    selected_user = st.sidebar.selectbox('Show analysis with respect to the users', user_list)
    if st.sidebar.button('Show Analysis'):


        num_messages, word, num_media_messages, link = helper.fetch_stats(selected_user,df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(word)
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.title(link)

        # Monthly Timeline
        st.title("Monthly Timeline")
        monthly_timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(monthly_timeline['time'], monthly_timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Activity map
        st.title('Activity Map')
        col1, col2 = st.columns(2)
        with col1:
            st.header("Most Busy Day")
            busy_day = helper.weekly_activity(selected_user, df)
            fig, ax = plt.subplots()
            ax.barh(busy_day.index, busy_day.values, color=[ '#d4ac0d', '#d68910', '#ca6f1e', '#ba4a00', '#dc7633'])
            st.pyplot(fig)

        with col2:
            st.header("Most Busy Month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.barh(busy_month.index, busy_month.values, color=[ '#d4ac0d', '#d68910', '#ca6f1e', '#ba4a00', '#dc7633'])
            st.pyplot(fig)


        # Heatmap
        st.title('Weekly Activity Map')
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)


        # Finding the busiest user in the group or individual user
        if selected_user == 'Overall':
            st.title("Most Interactive User")
            x, percent_df = helper.most_busy_user(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                # ax.bar(x.index,x.values,color="red")
                ax.bar(x.index,x.values,color=['#AF7AC5', '#9B59B6','#884EA0'])
                st.pyplot(fig)

            with col2:
                st.header("Percent of Message")
                st.dataframe(percent_df)

        # Wordcloud
        st.title('Word Cloud')
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # Most common words
        most_common_df = helper.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.bar(most_common_df[0],most_common_df[1], color=['#a93226', '#cb4335', '#884ea0', '#7d3c98', '#2471a3',
                                                           '#2e86c1', '#17a589', '#138d75','#229954', '#28b463',
                                                           '#d4ac0d', '#d68910', '#ca6f1e', '#ba4a00', '#dc7633' ])
        plt.xticks(rotation='vertical')
        st.title("Most Common Words")
        st.pyplot(fig)


        # emoji analysis
        emoji_df = helper.emoji_helper(selected_user, df)
        st.title("Emoji Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(5), labels=emoji_df[0].head(5), autopct="%0.2f")
            st.pyplot(fig)

