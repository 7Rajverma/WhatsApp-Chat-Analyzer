# WhatsApp Chat Analyzer

### Live Demo : https://whatsapp-chat-analyzer-p6l5.onrender.com

## Overview
The WhatsApp Chat Analyzer is a Streamlit-based web application that helps users analyze their WhatsApp chat data. 
It provides insights such as message statistics, activity patterns, word clouds, and emoji usage.

## Features
 • Upload a WhatsApp chat file and analyze it.
 • View total messages, words, media shared, and links sent.
 • Visualize monthly and daily messaging trends.
 • Analyze the most active days and times with heatmaps.
 • Identify the most interactive users in a group chat.
 • Generate a word cloud from chat messages.
 • Extract frequently used words (excluding common stop words).
 • Perform emoji analysis.

 ## Installation
    To run this project locally, follow these steps:

 ## Prerequisites
  • Python 3.7+
  • pip (Python package manager)

 ## Steps
   1.Clone the repository:
         git clone [https://github.com/your-username/whatsapp-chat-analyzer.git cd whatsapp-chat-analyzer](https://github.com/7Rajverma/WhatsApp-Chat-Analyzer.git).

   2.Install the required dependencies:
         pip install -r requirements.txt
         
   3.Run the application:
         streamlit run app.py

   ## Usage
        1.Open the application in a web browser (default: http://localhost:8501).
        2.Upload a WhatsApp chat file (.txt format exported from WhatsApp).
        3.Select a user (or choose "Overall" for group-wide analysis).
        4.Click "Show Analysis" to generate insights.

   ## File Structure     
          whatsapp-chat-analyzer/
      │── app.py             # Main Streamlit app
      │── helper.py          # Functions for analysis
      │── preprocessor.py    # Data preprocessing module
      │── stop_hinglish.txt  # Stop words list (Hinglish and English)
      │── requirements.txt   # Dependencies
      │── README.md          # Project documentation

   ## Dependencies
      The following Python libraries are used in this project:
        • streamlit
        • pandas
        • matplotlib
        • seaborn
        • wordcloud
        • emoji
        • urlextract

  ### Install them using:
      pip install streamlit pandas matplotlib seaborn wordcloud emoji urlextract

  ## Contributing
      Feel free to fork this repository and submit pull requests with improvements or new features.

  ## License
      This project is licensed under the MIT License.
                 
           
