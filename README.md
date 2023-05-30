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

- In Windows environment

  - cmd.exe shell

    `C:\> <venv>\Scripts\activate.bat`

  - PowerShell

    `PS C:\> <venv>\Scripts\Activate.ps1`

Then need to add requirements.txt file to install all the dependencies.

```
pip install -r requirements.txt
```

### How to set OpenAI API key

You need to have OpenAI API key to run the project. You can get the API key from [here](https://platform.openai.com/account/api-keys).

- for `WINDOWS` platform need to add OpenAI API key to environment variable. Using below command you can set OPENAI_API_KEY to environment variable.

  ```
   $Env:OPENAI_API_KEY =‘your_api_key_here’
  ```

- for `LINUX` environment need to add OpenAI API key to bashrc file. Using below command you can set OPENAI_API_KEY to bashrc file.

  ```
  export OPENAI_API_KEY=‘your_api_key_here’
  ```

---

Now you successfully setup the environment. Now you can run the project. To run the project you need to run the below command.

```
flask --app index run
```

## How to use the API

### Training API

To train the model you need to send a POST request to the below endpoint.

```
http://<host>:<port>/train
```

**The request body should be a with file data. The file should be a PDF file.**

### Ask Question API

To ask question you need to send a POST request to the below endpoint.

```
http://<host>:<port>/askQuestion
```

**The request body should be a JSON with below format.**

```
{
    "question": "What is the name of the company?"
}
```
