def detect_uncertainty(text):
    text = text.lower()
    uncertain_phrases = ["i'm fine", "ok", "nothing", "idk", "maybe"]
    
    for phrase in uncertain_phrases:
        if phrase in text:
            return True
    return False


def detect_excitement(text):
    text = text.lower()
    
    excitement_signals = ["😂", "😄", "😆", "!", "finally", "yay", "let's go", "omg", "woo", "yes"]
    
    for signal in excitement_signals:
        if signal in text:
            return True
            
    if text.count("!") >= 2:
        return True
        
    return False


def detect_frustration(text):
    text = text.lower()
    
    frustration_signals = ["not working", "still", "again", "why", "error", "issue", "😤", "ugh"]
    
    for signal in frustration_signals:
        if signal in text:
            return True
            
    if text.count("!") >= 2:
        return True
        
    return False


def detect_confusion(text):
    text = text.lower()
    
    confusion_signals = ["what should i do", "i don't understand", "how does this", "confused", "help me"]
    
    for signal in confusion_signals:
        if signal in text:
            return True
            
    return False