
start = input("SHALL WE BEGIN!!! :) (y/n): ")
while start == "y" : # here "while" condition used before whole block of code so that it repeats them in every loop.

  print('''

	Welcome to HOROSCOPE program 


	|*| ZODIAC SIGNS


    1.  Aries
 
    2.  Taurus
 
    3.  Gemini
 
    4.  Cancer
 
    5.  Leo
 
    6.  Virgo
 
    7.  Libra
 
    8.  Scorpio
 
    9.  Sagittarius
 
    10. Capricorn
 
    11. Aquarius 
 
    12. Pisces
	     ''') #this is what users gonna see at beginning as output

 

  zod = input("please type the no. beside your zodiac sign above : " ) 
  zod = int(zod)



  if 1 == zod : 
  	print('''There could be trouble brewing in the workplace, Aries. Some of your colleagues neither like nor trust each otherand find it impossible to work together. Adjustments are needed if everyone is going to work to the best of their abilities.
  		If you're in a position to handle this, do it now. If you aren't, distance yourself from the situation. It's the only way to stay sane!''')
  
  elif 2 == zod :
    print (''' Squabbles may come up between you and a sibling or neighbor, Taurus. Your ability to compromise is definitely called for here. If you aren't careful, this could turn into a battle of wills. The minute the disagreement comes up,
     try to talk it out and turn it into a win/win situation. Otherwise, things may be said that shouldn't be, and feelings could remain hurt for a long time.''')
  
  elif 3 == zod :
  	print(''' Money matters might cause you a few headaches, Gemini. You could be torn between the desire to put money aside for the future and the impulse to buy something 
  		that you've wanted for a long time. There may be a way to have it both ways. Save a little less and try to find a bargain price for your item. Take everything into consideration and work it out before you make yourself crazy''')
  
  elif 4 == zod :
  	print(''' Too much rigorous exercise over the past few days might have you feeling a little sore and tired, Cancer. Your nerves may be on edge, and you could be more likely than usual to snap at those around you.
  	 Try to ease both nerves and muscle aches by soaking in a hot bath. Herbal tea might also help. Accept that you should take it easy today and then do it!''')
  
  elif 5 == zod :
    print(''' Spiritual breakthroughs may have you feeling a little disconcerted, Leo. Clearing away deadwood, such as past traumas, might tell you a few things about yourself you'd rather not face.
     It's vital to release them in order to progress as a human being. Even if tears are involved, this is a positive development. You'll feel happier once it's all set free. Onward and upward!''')
  
  elif 6 == zod :
    print ('''  A virtual conference of some kind could touch upon some pretty volatile issues, Virgo. People could disagree to the point that the meeting turns into a shouting match. 
    	You probably have strong opinions on this as well, but don't get involved. You won't be able to stop the argument, and it can only cause you stress. If you can, avoid joining this meeting altogether. Think about it!''')
  
  elif 7 == zod :
  	print('''  Is your significant other caught up in family problems and unable to spend time with you? Don't let your insecurity get the best of you. Your partner needs to deal with family now.
  	 Relax, do what you want to do, and have confidence that you'll be spending more time together as soon as possible. After dealing with family quarrels, you'll be a peaceful refuge for your partner.''')
  
  elif 8 == zod :
  	print(''' Matters involving communication seem to be fouled up, Scorpio. Messages may not get delivered, emails may not go through, and people might misinterpret your words. This could create a mess that brings everything to a screeching halt.
  	 You need to speak to people directly, give detailed instructions, use simple language, and make sure they take notes, or beware of the consequences!''')
  
  elif 9 == zod :
  	print(''' Your values could oppose those of a business or romantic partner today, Sagittarius. One of you may be overly pragmatic and the other too idealistic. One seems callous, while the other seems to be living in a dream world.
  	 This could be a milestone in your relationship if approached properly. If you can't create a win/win situation, perhaps you should reconsider the partnership.''')
  
  elif 10 == zod :
    print (''' If you've been having trouble reaching a romantic partner, Capricorn, it might be a good idea to stop trying. Your friend is having a rough day and might not make the best company. 
    	In fact, your beloved could view a call from you as an unwelcome interruption and be short, if not downright rude. If you speak with your friend, keep it brief and plan to get together - just not today.''')
  
  elif 11 == zod :
  	print(''' You may feel a bit restless and unsettled without really knowing why, Aquarius. Stresses on the job could churn up repressed resentment from the past that you need to release. Try to discern exactly what these stresses remind you of.
  	 If you're unable to do this, however, you'll probably still reap the benefits of the release. Stay focused on your work and just let it happen.''')
  
  elif 12 == zod :
  	print('''  Too many people could be vying for your attention today, Pisces. All of them want advice or help. This could be flattering, and you'll probably want to help them, but it can also be unsettling and make it hard to focus. 
  		Don't let this set your temper on edge and cause you to snap at your friends. Take each request one at a time, make no promises, and do your best.''')
  
  else :
  	print("oh! please try enter correct response :) next time ") 
  start = input("you wanna continue? (y/n) : ")  # added here to modify while loop condition above and eventually provide exit condition for users

print("THANKS FOR USING THIS PROGRAMME(MY FIRST EVER TOO (●'◡'●) ) I HOPE YOU GUYS LIKED IT :) ")
  	
#email = kh143307@gmail.com
#name = kumar harsh