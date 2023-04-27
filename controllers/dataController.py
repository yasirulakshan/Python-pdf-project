class dataController:
    A = "sk-0pxxQ"
    P = "nATUPRy"
    I = "pWTlx6Ot"
    K = "T3BlbkFJI"
    E = "us4t9zQ3SG"
    Y = "4dU2MjeSU"

    open_ai_api_key = A+P+I+K+E+Y


    scenario = "You are an AI assistant built to help people." + "You are currently in a conversation with a human." + "To answer their questions, you are provided with necessary information in the Information Section below." + "If the answer is not found within the provided information, say \"I don\'t have that knowledge.\"" + "\n\n" + "Information Section:" + "\n\n"

    def getOpenAIAPIKey(self):
        return self.open_ai_api_key

    def getConstructedChat(self,information, question):
        return self.scenario + information + '\n\nQ:' + question