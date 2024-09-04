import EmotionDetection

def test_emotion_detection():
    state1='I am glad this happened'
    state2='I am really mad about this'
    state3='I feel disgusted just hearing about this'
    state4='I am so sad about this'
    state5='I am really afraid that this will happen'
    res1=EmotionDetection.emotion_detector(state1)
    assert res1['dominant_emotion']=='joy'
    res2=EmotionDetection.emotion_detector(state2)
    assert res2['dominant_emotion']=='anger'
    res3=EmotionDetection.emotion_detector(state3)
    assert res3['dominant_emotion']=='disgust'
    res4=EmotionDetection.emotion_detector(state4)
    assert res4['dominant_emotion']=='sadness'
    res5=EmotionDetection.emotion_detector(state5)
    assert res5['dominant_emotion']=='fear'
    print('all pass')

if __name__=='__main__':
    test_emotion_detection()