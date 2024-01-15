# youtube-app
Helps you to learn a language by quizzing you on YouTube videos in different languages.

```
pip install requirements.txt
```

## Inspiration

It is known that the best way to learn a language is to immerse yourself in the media of that language. However, watching media is traditionally a passive process, which has been indicated in many studies to have limited effectiveness in knowledge retention. Our goal was to innovate a solution that transforms the act of video watching into an active, engaging process, ultimately enhancing language learning and expediting the acquisition of new languages for our users.

## What it does

linquiztics analyzes the video you are watching and creates a list of questions using AI that evaluates your understanding of the content of the video and provides detailed feedback on how the user can improve their understanding of the content. Not only does it have the functionality of playing audio for learning the pronunciation, it also can interpret the words that the user is saying for input.

## How we built it

Leveraging Taipy for both the frontend and backend development, we seamlessly integrated various APIs to enhance our project's functionality. By tapping into YouTube's API, we efficiently retrieved video transcripts, which were then processed through OpenAI's GPT to dynamically generate quiz questions. Introducing the Whisper API allowed us to incorporate voice input, enabling users to engage in vocal practice during the quiz. Furthermore, we employed gTTS to implement an auditory component, integrating sound playback for an immersive pronunciation learning experience. 

