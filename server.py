'''server file for emotion detection'''
from flask import Flask, request, render_template
import EmotionDetection

app=Flask(__name__)

@app.route('/')
def index():
    '''this is the index'''
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector():
    '''this is the emotion detector function'''
    text=request.args.get('textToAnalyze')
    result=EmotionDetection.emotion_detector(text)
    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again'
    result_txt='For the given statement, the system response is '
    result_txt+=', '.join([f"'{k}': {v}"for k,v in result.items()][:-1])
    result_txt+=f". The dominant emotion is {result['dominant_emotion']}."
    return result_txt

if __name__=='__main__':
    app.run(debug=True)
