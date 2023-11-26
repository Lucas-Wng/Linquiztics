import taipy as tp
import makequestions

from taipy import Config

input_name_data_node_cfg = Config.configure_data_node(id="input_name")
message_data_node_cfg = Config.configure_data_node(id="message")
questions_array_data_node_cfg = Config.configure_data_node(id="questions_array")
answers_array_data_node_cfg = Config.configure_data_node(id="answers_array")
qnum_data_node_cfg = Config.configure_data_node(id="qnum")


page = """
<|container|
# **linquiztics**{: .color-secondary}
<br/>

<|layout|columns=1 1 1|gap=30px|class_name=card|

<link|
## **Video**{: .color-primary} Link

<|{input_name}|input|label=Paste link here first!|>
<|submit|button|on_action=submit_scenario|>
|link>


<language|
## **Language**{: .color-primary}

<|{language}|selector|lov={[("en", "English"), ("sp", "Spanish"), ("ko", "Korean")]}|dropdown=True|>
|language>

<difficulty|
## Difficulty

<|{difficulty}|selector|lov={[("easy", "Easy"), ("medium", "Medium"), ("hard", "Hard")]}|dropdown=True|>
|difficulty>
|>

<|layout|columns=1|gap=30px|class_name=card|
### Question: 
<|{message}|text|>
<br/>
<br/>
### Your Answer: 
<|{answer}|input|class_name=fullwidth|>
<br/>
<|{feedback}|text|>
<br/>
<|submit|button|on_action=submit_answer|>

<br/>
<|next|button|on_action=change_text|>
|>

|>

<style>
button {text-align: center;}
</style>
"""

input_name = None
message = None
language = 'en'
difficulty = None
answer = None
feedback = None

questions_array = []
answers_array = []

qnum = 0


def submit_scenario(state):
    state.qnum = 0
    state.questions_array, state.answers_array = makequestions.linkToQs(state.input_name, state.language[1])
    state.message = state.questions_array[0]

def submit_answer(state):
    evaluation, feedback = makequestions.confidence(state.answer, state.answers_array[state.qnum])
    evaluation = int(evaluation)
    print(evaluation)
    print(feedback)
    if evaluation == 0:
        state.feedback = "Incorrect.\n"+feedback
    elif evaluation == 1:
        state.feedback = "Mostly correct.\n"+feedback
    elif evaluation == 2:
        state.feedback = "Correct!\n"+feedback
    
def change_text(state):
    state.qnum += 1
    if state.qnum >= len(state.questions_array):
        state.message = "No more questions!"
        return
    state.message = state.questions_array[state.qnum]
    state.answer = ""
    state.feedback = ""

if __name__ == "__main__":
    tp.Core().run()
    tp.Gui(page).run()



