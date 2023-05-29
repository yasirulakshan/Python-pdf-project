# Question and Answering bot from our own PDF

---

The Question and Answering (Q&A) Bot is a powerful system that uses FAISS indexing and Langchain technology. It offers two endpoints for training and querying. The training endpoint processes PDF documents, creating indexes for fast retrieval. The querying endpoint allows users to ask questions and receive accurate answers based on the indexed information. With the Q&A Bot, users can extract valuable insights from large volumes of data with time and cost efficiently. Check the documentation for integration instructions.

## How to setup environment

First need to create python virtual environment.

```
python -m venv /path/to/new/virtual/environment
```

Then need to activate Virtual Environment

- In Linux environment

  - In bash/zsh shell

    `$ source <venv>/bin/activate`

  - In fish shell

    `$ source <venv>/bin/activate.fish`

  - csh/tcsh shell

    `$ source <venv>/bin/activate.csh`

  - PowerShell

    `$ <venv>/bin/Activate.ps1`
