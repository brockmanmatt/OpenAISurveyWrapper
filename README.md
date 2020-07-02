# OpenAI Survey Wrapper
> wrapper to label survey respones and test accuracy


## Install

`pip install OpenAISurveyWrapper`

## How to use

Fill me in please! Don't forget code examples:

```python
print("in progress")
```

    in progress


## Create and Add Key

```python
from OpenAISurveyWrapper.survey import survey
import json, pandas as pd
```

```python
tmp = survey()
tmp.add_key(json.load(open("../gpt3/key.json", "r"))["key"])
```

```python
term = "Federal Budget"
definition="refers to mentions of how the federal government budgets and spends its money."
tmp.addDefinition(term, definition)
```

```python
df = pd.read_excel("../combinedata.forml.xlsx")
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>text</th>
      <th>type</th>
      <th>classification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Abortions</td>
      <td>survey</td>
      <td>abortion</td>
    </tr>
    <tr>
      <td>1</td>
      <td>they shouldnt be stopping women from getting a...</td>
      <td>survey</td>
      <td>abortion</td>
    </tr>
    <tr>
      <td>2</td>
      <td>religion trying to control people either with ...</td>
      <td>survey</td>
      <td>abortion</td>
    </tr>
    <tr>
      <td>3</td>
      <td>abortion</td>
      <td>survey</td>
      <td>abortion</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Protecting abortion access and the Roe v Wade ...</td>
      <td>survey</td>
      <td>abortion</td>
    </tr>
  </tbody>
</table>
</div>



```python
tmp.loadExamplesFromDataFrame(df[["text", "classification"]].fillna(""))
```

```python
tmp.tryLabels(n=20, verbose=True)
```

    A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:
    post: "{}"
    q: Does this post primarily about Federal Budget (yes or no)?
    a:
    before
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "Norwegians on social media also questioned the attractiveness of immigrating to a country without free health care, paid parental leave or gun control.  “I’m a Norwegian who enjoyed studying & working in the US. The only thing that would attract me to emigrate to the US is your vibrant multicultural society. Don’t take that away.” -Jan Egeland, the head of the Norwegian Regugee Council. [The Washington Post]"\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     yes
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "Aha!  Another Swamp Man feeding at the public trough while so many of our Veterans are homeless and suffering from disabilities resulting from their Service to this country. "\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     Yes
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "rising inflation"\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     yes
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "It is terrible to see protesters in the face of conservative legislatures, but it is just as bad to see protesters from the other side of the philosophical isle  show extremely bad taste in expressing their discontent. These folks , no matter their political persuasion are trash and do not help constructively in the ongoing national discourse.  ---  "\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     Yes
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "27 Pediatricians were just fired from a Dallas medical facility and replaced with mid-levels. We have to do something. This has to stop. The rest is copied from Dr. Falcon’s page.   The trend of having employed physicians just “sign off” on mid level charts without allowing them to ACTUALLY supervise them is pervasive now, with the push for “cheaper” care by many hospitals without concern for patient safety.     They want to use our liability so when something goes wrong, they can blame a person who wasn’t even there and didn’t even get to teach/provide care Bc it’s not time or cost efficient.     MEDICINE is not ABOUT MONEY.  It’s about taking care of patients.  A mid level with two days training has no business taking care of patients independently-  a first year medical student is about as qualified.   That doesn’t inspire confidence, does it?    What can you do?  Always ask who is providing your care.  What are their credentials?  Is their supervising physician (if they have one) even on site for consultations??   Ask at every Clinic and Hospital you go to.  If they say no, ask to see a physician.  And if the answer is no, LEAVE.   And make sure you leave a review or comment to the facility as to why.    What can we doctors do? Refuse to participate in this sham that medicine has become.  Do not work for a company that requires you to blindly sign off on mid level charts for patients you’ve never met.  Yes, there will be consequences, until we stand together.  (Anyone see"\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     No
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "consumers"\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     yes
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "Why are people obsessed with tossing out the baby with the bathwater?  ICE is broken.  Get rid of it.  Obamacare doesn\'t work.  Get rid of it.  Medicaid doesn\'t work.  Get rid of it.  Medicare isn\'t perfect.  Ditch it.  Congress is broken.  Very broken.  Get rid of it.  If your children disappoint you, do you toss them out of your life for good?  Or does common sense prevail with you steering them in the right direction?  Why can\'t we take a broken program that started with good intentions, and concentrate on making things right?  Go back to the original plans, view the intent, and make the program work for the country."\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     No.
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "Got my tragus done today."\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     No.
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "The war on guns -- 2nd amendment issues "\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     yes
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "the pee pee tape and what Putin has on Dump"\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     No
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "Good Sunday morning FB family and friends. Mass this morning then some grocery shopping for much needed items Dylan did not do well in his first two matches but I pray he does not get discouraged. There are over 5100 wrestlers from all over the US. It is such an honor just to have been selected. Daniel has arrived in PA for his wrestling camp. Pray for his safety. But first let us begin our day with prayers for our little group in need of them: John, Alex, Charles, Paul, Don, Mike, Brandon, Buddy, Roch, Fred, Amy, Bridget, Beverly(2), Alex, Sarah Grace, Valerie(2), Jeanette, Kelly, Katie, Cindy &John, my friends in A\'ville, TX, Lafayette, and myself. Marie mixed some oils together and brought them to me yesterday. Seems to have helped with swelling and stiffness. Please, God, shower our group with your healing graces. Pray also for world peace and a positive change in the attitude of our society. July 15, 2018 You\'ll find when you smile, your day will be brighter and all of your burdens will seem so much lighter. HSR Praise be the Lord, our God our Savior, who daily bears our burdens. Psalm 68:19 This is a day to smile. I have been telling all of you everyday is a day to smile. Whoever smiles often, often brightens the day and lightens the burden. Go out into your little corner of the world and smile. Be kind, patient, forgiving, loving, happy, grateful and prayerful. Have a super good Sunday."\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     No
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "the division between people that has increased tremendously under Trump."\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     yes
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "Classic windmill, Dutch countryside"\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     No
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "WANTING TO TAKE FIRE ARMS"\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     yes
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "Yes, yes, yes! Women are policed about their clothes, their looks, whether they smile or not. Do dudes have to deal with this? NO! (And if it\'s a yes, please share, I\'d love to hear your experience)."\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     No.
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "This was an act of "domestic terrorism" by a repulsive, brain-dead fascist. Trump and his administration needs to acknowledge this. Otherwise, he and his administration will be seen as being on board with these evil bastards and their violent actions.   "\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     Yes
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "That was an interception!!!"\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     No
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "Hatred"\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     yes
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "Israel has become a burdensome stone to all nations. No one can accept  Jersalem as the TRUE capital of Isreael but want to call it Capital of Palestine. To those call bible fables take a hard look around you. Satan the accuser and father of lies has you so blinded from the truth.   Zechariah 12:3  And in that day will I make Jerusalem a burdensome stone for all people: all that burden themselves with it shall be cut in pieces, though all the people of the earth be gathered together against it."\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     No.
    {'prompt': 'A post is about Federal Budget if it refers to mentions of how the federal government budgets and spends its money. Consider the following post:\npost: "A very interesting read. Impeaching 45 has been discussed since he was inaugurated and I\'ve been conflicted up until now. The article discusses both of the arguments against impeaching: (1) Pence would be president and he might actually get things done and (2) it sets up a situation where congress potentially impeaches any president they disagree with.   If we as a nation don\'t impeach this person, who is clearly unfit and perhaps dangerous, then what is impeachment for? Rather than set up a slippery slope, dealing reasonably with somebody who needs to be removed would restore some dignity to our country\'s government.   Let Pence be president, I may not agree with his policies, but at least he wouldn\'t be a laughing stock and how much more damage could he really do than what is being done now? If the GOP wants to retaliate in the future by impeaching a Democratic president, so be it. We can weather that. It\'s beyond time for us to do something."\nq: Does this post primarily about Federal Budget (yes or no)?\na:', 'engine': 'davinci', 'temperature': 0, 'max_tokens': 10, 'stop': '\n'}
     Yes.
    after
    [' yes', ' Yes', ' yes', ' Yes', ' No', ' yes', ' No.', ' No.', ' yes', ' No', ' No', ' yes', ' No', ' yes', ' No.', ' Yes', ' No', ' yes', ' No.', ' Yes.']


```python
tmp.labeled
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data</th>
      <th>label</th>
      <th>Federal Budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1035</td>
      <td>Norwegians on social media also questioned the...</td>
      <td>immigration</td>
      <td>yes</td>
    </tr>
    <tr>
      <td>2389</td>
      <td>Aha!  Another Swamp Man feeding at the public ...</td>
      <td>poverty</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>126</td>
      <td>rising inflation</td>
      <td>economy</td>
      <td>yes</td>
    </tr>
    <tr>
      <td>2289</td>
      <td>It is terrible to see protesters in the face o...</td>
      <td>party politics</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>963</td>
      <td>27 Pediatricians were just fired from a Dallas...</td>
      <td>healthcare</td>
      <td>No</td>
    </tr>
    <tr>
      <td>1325</td>
      <td>consumers</td>
      <td>none</td>
      <td>yes</td>
    </tr>
    <tr>
      <td>968</td>
      <td>Why are people obsessed with tossing out the b...</td>
      <td>healthcare</td>
      <td>No.</td>
    </tr>
    <tr>
      <td>2124</td>
      <td>Got my tragus done today.</td>
      <td>none</td>
      <td>No.</td>
    </tr>
    <tr>
      <td>792</td>
      <td>The war on guns -- 2nd amendment issues</td>
      <td>gun control</td>
      <td>yes</td>
    </tr>
    <tr>
      <td>515</td>
      <td>the pee pee tape and what Putin has on Dump</td>
      <td>foreign affairs</td>
      <td>No</td>
    </tr>
    <tr>
      <td>1532</td>
      <td>Good Sunday morning FB family and friends. Mas...</td>
      <td>none</td>
      <td>No</td>
    </tr>
    <tr>
      <td>2569</td>
      <td>the division between people that has increased...</td>
      <td>trump as issue</td>
      <td>yes</td>
    </tr>
    <tr>
      <td>387</td>
      <td>Classic windmill, Dutch countryside</td>
      <td>energy and environment</td>
      <td>No</td>
    </tr>
    <tr>
      <td>801</td>
      <td>WANTING TO TAKE FIRE ARMS</td>
      <td>gun control</td>
      <td>yes</td>
    </tr>
    <tr>
      <td>1573</td>
      <td>Yes, yes, yes! Women are policed about their c...</td>
      <td>none</td>
      <td>No.</td>
    </tr>
    <tr>
      <td>69</td>
      <td>This was an act of "domestic terrorism" by a r...</td>
      <td>crime</td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>1774</td>
      <td>That was an interception!!!</td>
      <td>none</td>
      <td>No</td>
    </tr>
    <tr>
      <td>1463</td>
      <td>Hatred</td>
      <td>none</td>
      <td>yes</td>
    </tr>
    <tr>
      <td>662</td>
      <td>Israel has become a burdensome stone to all na...</td>
      <td>foreign affairs</td>
      <td>No.</td>
    </tr>
    <tr>
      <td>1056</td>
      <td>A very interesting read. Impeaching 45 has bee...</td>
      <td>impeachment</td>
      <td>Yes.</td>
    </tr>
  </tbody>
</table>
</div>


