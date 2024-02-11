import json
import requests

str_list = ["All our dreams can come true, if we have the courage to pursue them",
            "Everything you’ve ever wanted is on the other side of fear. 	",
            "Success is not final, failure is not fatal: it is the courage to continue that counts. ",
            "Hardships often prepare ordinary people for an extraordinary destiny. 	",
            "Believe in yourself. You are braver than you think, more talented than you know, and capable of more than you imagine. ",
            "I learned that courage was not the absence of fear, but the triumph over it. The brave man is not he who does not feel afraid, but he who conquers that fear. 	",
            "It does not matter how slowly you go as long as you do not stop",
            "There is only one thing that makes a dream impossible to achieve: the fear of failure. 	",
            " It’s not whether you get knocked down. It’s whether you get up. 	",
            "Your true success in life begins only when you make the commitment to become excellent at what you do. ",
            "Believe in yourself, take on your challenges, dig deep within yourself to conquer fears. Never let anyone bring	you down. You got to keep going. 	",
            "Definiteness of purpose is the starting point of all achievement. 	",
            "Too many of us are not living our dreams because we are living our fears. 	",
            "If you believe it will work out, you’ll see opportunities. If you believe it won’t, you will see obstacles. 	",
            "Permanence, perseverance and persistence in spite of all obstacles, discouragements, and impossibilities: It is	this, that in all things distinguishes the strong soul from the weak. 	",
            "Success means doing the best we can with what we have. Success is the doing, not the getting; in the trying, not the triumph. Success is a personal standard, reaching for the highest that is in us, becoming all that we can be.	",
            "If you set goals and go after them with all the determination you can muster, your gifts will take you places that will amaze you.	",
            "Hard times don’t create heroes. It is during the hard times when the ‘hero’ within us is revealed. 	",
            "Believe you can and you’re halfway there. 	",
            "Your mind is a powerful thing. When you fill it with positive thoughts, your life will start to change. 	",
            "Start by doing what’s necessary; then do what’s possible; and suddenly you are doing the impossible. 	",
            "I attribute my success to this: I never gave or took any excuse. 	",
            "Whatever you hold in your mind on a consistent basis is exactly what you will experience in your life. 	",
            "Most of the important things in the world have been accomplished by people who have kept on trying when	there seemed to be no hope at all. 	",
            "Strength does not come from physical capacity. It comes from an indomitable will.	",
            "Perseverance is the hard work you do after you get tired of doing the hard work you already did.	",
            "The future belongs to those who believe in the beauty of their dreams 	",
            "I am not a product of my circumstances. I am a product of my decisions. 	",
            "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart. 	",
            "You’re going to go through tough times – that’s life. But I say, ‘Nothing happens to you, it happens for you.’ See	the positive in negative events. 	",
            "Character cannot be developed in ease and quiet. Only through experience of trial and suffering can the soul be strengthened, ambition inspired, and success achieved.	",
            "If you can tune into your purpose and really align with it, setting goals so that your vision is an expression of that purpose, then life flows much more easily. 	",
            "Whatever the mind can conceive and believe, it can achieve. 	",
            "Don’t wish it were easier. Wish you were better. 	",
            "It is during our darkest moments that we must focus to see the light. ",
            "It’s not about perfect. It’s about effort. And when you bring that effort every single day, that’s where transformation happens. That’s how change occurs. 	",
            "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what	you are doing or learning to do.	",
            "Strength doesn’t come from what you can do. It comes from overcoming the things you once thought you couldn’t. 	",
            "Learn from the past, set vivid, detailed goals for the future, and live in the only moment of time over which you have any control: now. 	",
            "We don’t develop courage by being happy every day. We develop it by surviving difficult times and challenging adversity.	",
            "Fortune always favors the brave, and never helps a man who does not help himself. ",
            "Go confidently in the direction of your dreams. Live the life you have imagined. 	",
            "If you can dream it, then you can achieve it. You will get all you want in life if you help enough other people get	what they want.	",
            "The only person you are destined to become is the person you decide to be.	",
            "Perfection is not attainable, but if we chase perfection we can catch excellence. 	",
            "Life is 10% what happens to you and 90% how you react to it. 	",
            "If you don’t like something, change it. If you can’t change it, change your attitude. 	",
            "You control your future, your destiny. What you think about comes about. By recording your dreams and goals	on paper, you set in motion the process of becoming the person you most want to be. Put your future in good	hands – your own. 	",
            "Failure will never overtake me if my determination to succeed is strong enough. 	",
            "Inaction breeds doubt and fear. Action breeds confidence and courage. If you want to conquer fear, do not sit	home and think about it. Go out and get busy. 	",
            "Limitations live only in our minds. But if we use our imaginations, our possibilities become limitless. 	",
            "Setting goals is the first step into turning the invisible into the visible. 	",
            "Success means doing the best we can with what we have. Success is the doing, not the getting; in the trying, not the triumph. Success is a personal standard, reaching for the highest that is in us, becoming all that we can be.	",
            "Only those who dare to fail greatly can ever achieve greatly.	",
            "Remember that not getting what you want is sometimes a wonderful stroke of luck.	",
            "Staying positive does not mean that things will turn out okay. Rather it is knowing that you will be okay no matter how things turn out. 	",
            "You gain strength, courage, and confidence by every experience in which you really stop to look fear in the	face. You are able to say to yourself, ‘I lived through this horror. I can take the next thing that comes along. 	",
            "No matter how hard times may get, always hold your head up and be strong; show them you’re not as weak as they think you are. 	",
            "We may encounter many defeats but we must not be defeated. 	"]

for item in str_list:
    quote = fr'{item.strip()}'
    payload = json.dumps({
        "quote": f"{quote}",
        "author": "",
        "tags": []
    })

    url = "http://localhost:90/quote/add"
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.status_code)
    except Exception as e:
        print(e)
