# sign-language
This repository is about end to end communication between physically hearing impairment(person1) and outer world(person2).

from person1 to person2:
<br>
1.person 2 records the video of signs generated by person1.
<br>
2.the video is split into frames and body poses are taken from the frames. 
<br>
3.from body points and locations we map the sign gloss.
<br>
4.from sign gloss to english is translated through NLP techniques.

from person2 to person1:
<br>
1.person 1 records the english text generated by person2.
<br>
2.the english words are then translated to sign gloss using NLP techniques.
<br>
3.body points are generated from sign gloss.
<br>
4.Using  GAN video is generated.

** NLP techniques output**


**Video generation using GAN.**



![sign2](https://user-images.githubusercontent.com/48018142/66250873-3f86f380-e766-11e9-8680-49925ccf8211.JPG)
![sign1](https://user-images.githubusercontent.com/48018142/66250887-562d4a80-e766-11e9-8295-183c7f104b6b.JPG)
