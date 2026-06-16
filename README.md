# Technical Documentation for Sentiment Analysis
### Introduction
The Sentiment Analysis System is a Natural Language Processing (NLP) application developed to identify the emotional tone of textual messages. The system analyses short conversational texts and classifies them into positive, negative, or neutral sentiments. It is specifically designed for handling social media content, chat messages, and informal conversational language commonly found in online communication platforms.

The Sentiment Analysis API is responsible for handling API requests, processing user text, performing sentiment prediction, and returning structured responses. The backend is designed using a modular architecture to ensure clean code organization, scalability, and easier maintenance.
The system processes text input and classifies sentiment into categories such as:
- Positive
- Negative
- Neutral

The backend structure separates routing, business logic, and utility functions into different layers for better software design.


### Objectives

- To develop a backend API system capable of analyzing user text and predicting sentiment accurately.
- To classify text into sentiment categories such as positive, negative, and neutral.
- To create a modular and scalable backend architecture for easier maintenance and future development.
- To preprocess and clean textual data before performing sentiment prediction.
- To integrate Natural Language Processing (NLP) techniques for better text understanding.
- To support easy testing, debugging, and deployment of the backend application.
- To provide fast and efficient sentiment prediction for real-time applications.

### Folder Architecture
This backend architecture provides a clean and scalable structure for building a Sentiment Analysis API system. The layered design separates routing, business logic, and utility functions, making the application easy to understand, maintain, and extend for future development. 
```
backend/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   └── models.py
│   │
│   ├── routes/
│   │   └── sentiment_routes.py
│   │
│   ├── schemas/
│   │   └── sentiment_schema.py
│   │
│   ├── services/
│   │   └── sentiment_service.py
│   │
│   ├── repositories/
│   │   └── sentiment_repository.py
│   │
│   └── utils/
│       └── text_cleaner.py
│
├── requirements.txt
│
└── run.py
```

### Technology Stack

| Technology / Tool          | Purpose                                                           |
| -------------------------- | ----------------------------------------------------------------- |
| Python                     | Programming language used for development                         |
| FastAPI                    | Creation of REST APIs and request handling                        |
| Uvicorn                    | Running and serving the FastAPI application                       |
| VADER Sentiment Analyzer   | Lexicon-based sentiment analysis and scoring                      |
| RoBERTa Sentiment Model    | Transformer-based sentiment analysis for contextual understanding |
| PostgreSQL                 | Storage of chat and sentiment data                                |
| SQLAlchemy                 | ORM for database interaction and query management                 |
| Pydantic                   | Data validation and request/response schemas                      |
| Postman                    | API testing and endpoint validation                               |
| Regular Expressions (`re`) | Text cleaning and preprocessing                                   |
| APIRouter                  | Organizing APIs into separate route modules                       |
| Visual Studio Code         | Code development and debugging                                    |
| Hugging Face Transformers  | Loading and running transformer-based sentiment models            |
| UUID                       | Unique identifier generation for database records                 |
| Git & GitHub               | Version control and source code management                        |


### System Architecture

![Alt Text]()
