# AI - Voice Assistant Pro

#### Welcome to the world of our Voice Assistant Pro, a potent tool that assists you in accomplishing a multitude of tasks. It leverages machine learning and natural language processing to provide a natural & intuitive user experience. Now, you have the power to interact with your computer by merely speaking to it.
#### For an impressive demo of this project, watch this [YouTube video](https://www.youtube.com/watch?v=ErR-vdYssv0)
#### Click here for the comprehensive [Project Report](https://github.com/BossLu93/AI-Voice-Assistant-Pro/blob/main/Project%20Report%20GitHub.pdf)

## Features
Our AI Voice Assistant Pro is equipped with numerous features, such as:
- Offering jokes to make you smile.
- Presenting the latest news headlines for keeping you updated.
- Revealing your IP address for facilitating connectivity.
- Providing the latest updates about movies & TV series.
- Furnishing current weather reports for any city and using the IP address for precise local weather updates.
- Assessing your internet speed for optimum connectivity.
- Providing system stats, including RAM & CPU usage, battery percentage, and system specifications.
- Generating an image from the user-provided text.
- Facilitating emails for seamless communication.
- Accomplishing system operations like opening, closing, switching tabs; copying, pasting, deleting, and selecting text; creating new files; minimizing, maximizing, switching, closing windows etc.
- Taking screenshots for capturing significant moments.
- Offering brief information (3 sentences) on any topic or personality.
- Performing math operations and answering general queries and GK questions.
- Opening apps and websites for increased productivity.
- Taking notes for tracking important information.
- Saving chat history for future reference.
- Executing Google searches for relevant information.
- Playing songs and videos on YouTube for leisure.
- Displaying maps of any city and calculating distance between two destinations via Google Maps.<br>

NOTE: To enable the AI Voice Assistant Pro to send emails, turn on the "Less secure apps" option in your Gmail account. Click [here](https://myaccount.google.com/lesssecureapps) to enable access.

## API Keys
You need to register for several API keys to run this program. Register your API key by clicking the following links
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Wolframaplha API](https://products.wolframalpha.com/api)
- [News API](https://newsapi.org/)
- [TMDB API](https://developers.themoviedb.org/3/getting-started/introduction)
- [DreamStudio API](https://platform.stability.ai/docs/getting-started/authentication)

## Installation

Ensure that `Python` and `pip` are installed in your system before proceeding.

Open command prompt and navigate to your home directory.

Clone the repository using
```
git clone https://github.com/BossLu93/AI-Voice-Assistant-Pro.git
```

Navigate to the project directory
```
cd AI-Voice-Assistant-Pro
```

Acquire necessary API keys and open the file `AI-Voice-Assistant-Pro/Data/.env` to insert the keys in the designated placeholder fields.

Run the setup script
```
python setup.py
```

Navigate to the `AI-Voice-Assistant-Pro/Plugins/` and run this command to start the AI Voice Assistant Pro.
```
python main.py
```

You are ready to go! AI Voice Assistant Pro should be operational now.

## Code Structure

    ├── AI-Voice-Assistant-Pro
        ├── Data                              
            ├── .env                          # Stores API keys, email, and password.
            ├── chat_model                    # Directory that stores the trained model used to understand user's intent
            ├── chats.db                      # Database file that stores chat history
            ├── intents.json                  # Data on which the model is trained
            ├── label_encoder.pickle          # Converts text labels into numerical values
            └── tokenizer.pickle              # Splits the text into separate tokens
        ├── Plugins
            ├── API_functionalities.py        # Contains functions that interact with different APIs
            ├── browsing_functionalities.py   # Contains functions for web browsing
            ├── database.py                   # Contains functions for interacting with chat history database
            ├── gmail.py                      # Contains functions for sending emails
            ├── image_generation.py           # Contains functions for generating images from text
            ├── main.py                       # It is the starting point of the AI Voice Assistant Pro
            ├── model_training.py             # Contains functions for training the intent recognition model
            ├── system_operations.py          # Contains functions for system operations
            └── websites.py                   # Contains a list of websites that can be opened by the AI Voice Assistant Pro
        ├── requirements.txt                  # Lis