#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd 
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
from PIL import Image

df = pd.read_csv('wanted.csv')


# In[2]:


df['Days_on_List'] = df['Days_on_List'].apply(lambda x: x.split('days')[0])
df['Days_on_List'] = df['Days_on_List'].astype(int)
df.info()


# In[23]:


img = Image.open("FBI.png")
st.image(img, width=200)


# In[4]:


st.title('FBI Wanted List')


# In[5]:


st.subheader('Inleiding')
'De afgelopen weken is de naam Gabby Petito vaak voorbij gekomen. Gabby Petito is een jonge vrouw van 22 jaar oud. Tijdens een roadtrip met haar vriend is ze vermist geraakt. Na een tijd als vermist persoon kwam op op 19 september 2021 het tragische nieuws dat haar stoffelijk overschot is gevonden in Bridger-Teton National Forest in Wyoming. Omdat dit ons aansprak is er gekeken of er een dataset bestaat in het teken van misdaad. Zo zijn we terecht gekomen bij een dataset van de FBI. De FBI heeft een API vrij gegeven met alle mensen die gezocht worden. Deze personen worden gezocht om verschillende redenen. Denk hierbij aan vermist zijn maar ook het plegen van een moord.'


# In[1]:


'In dit blog wordt gekeken naar mogelijke verbanden tussen de verschillende variabelen van de personen op de lijst van gezochte.'


# In[7]:


''


# In[8]:


''


# In[9]:


st.subheader('Data Frame')
'In onderstaande tabel is het dataframe te zien die gebruikt wordt voor de analyses. De tabel bestaat uit verschillende variabelen. In de API staan meerdere variabelen die overbodig zijn voor de analyses, deze staan niet in het dataframe. De variabelen die rechtstreeks uit de API komen zijn: "Name",  "Reward in $" en "Publication date". Middels data manipulatie zijn er nog vier variabelen toegevoegd. "Why on list", "Days on list" en "Sex". Dit is gedaan in google met de hand omdat het maar een paar personen zijn. Moord en vermissing zijn de meest voorkomende redenen dat de personen op de lijst staan. De hoeveelheid dagen dat de personen op de lijst staan verschilt. Het varieert tussen twaalf dagen en 4041 dagen. Ook is opvallend dat er meer mannen zijn die een misdaad gepleegd hebben dan vrouwen. Om verbanden en de analyses die gemaakt zijn weer te geven zijn er drie visualisaties gemaakt.'


# In[10]:


st.dataframe(df)


# In[11]:


''


# ## Graphs

# In[12]:


st.subheader('1. Checkbox')
'De checkbox heeft de mogelijkheid om aan te geven in hoeveel van de zaken de persoon in kwestie een man of een vrouw is. Door bijvoorbeeld op "Vrouw" klikken krijgt u een overzicht van de gevallen waar een vrouw de persoon in kwestie is.'


# In[13]:


#Checkboxes
fig_all_sex = px.bar(df, x='Name', y='Reward in $')
fig_male = px.bar(df[df['Sex'] == 'Male'], x='Name', y='Reward in $')
fig_female = px.bar(df[df['Sex'] == 'Female'], x='Name', y='Reward in $')

fig_all_sex.update_layout({'xaxis':{'title':{'text': 'Naam'}},
                   'yaxis':{'title':{'text':'Beloning in $'}},
                   'title':{'text':'FBI Wanted Beloning in Dollars', 
                            'x':0.5}})

fig_male.update_layout({'xaxis':{'title':{'text': 'Naam'}},
                   'yaxis':{'title':{'text':'Beloning in $'}},
                   'title':{'text':'FBI Wanted Beloning in Dollars', 
                            'x':0.5}})

fig_female.update_layout({'xaxis':{'title':{'text': 'Naam'}},
                   'yaxis':{'title':{'text':'Beloning in $'}},
                   'title':{'text':'FBI Wanted Beloning in Dollars', 
                            'x':0.5}})


# In[14]:


#Checkboxes
male = st.checkbox('Man', key=1)
female = st.checkbox('Vrouw', key=2)

if male == False and female == False:
    st.plotly_chart(fig_all_sex)

if male == True and female == False:
    st.plotly_chart(fig_male)
    
if female == True and male == False:
    st.plotly_chart(fig_female)

if male == True and female == True:
    st.error('Selecteer één optie')


# #### ---

# In[15]:


''


# In[16]:


st.subheader('2. Dropdown')
'Bij onderstaande grafiek is een dropdown functie toegevoegd. In het menu van de dropdown kan gekozen worden voor één bepaalde staat of alle staten. Wanneer er op een staat geklikt wordt geeft de grafiek de naam van de gezochte persoon aan en hoelang die persoon al op de lijst van de FBI staat.'


# In[17]:


#Dropdown
fig2= go.Figure()
for state in df['State'].unique():
    df1=df[df.State == state]
    fig2.add_trace(go.Bar(x=df1['Name'], y=df1['Days_on_List'],  name=state))
    
dropdown_buttons = [
    {'method': 'update', 'label': 'Alle','args': [{'visible': [True, True, True, True, True, True, True, True, True, True, True, True, True]}]},
    {'method': 'update', 'label': 'Ohio','args': [{'visible': [True, False, False, False, False, False, False, False, False, False, False, False, False]}]}, 
    {'method': 'update', 'label': 'New York','args': [{'visible': [False, True, False, False, False, False, False, False, False, False, False, False, False]}]}, 
    {'method': 'update', 'label': 'New Mexico','args': [{'visible': [False, False, True, False, False, False, False, False, False, False, False, False, False]}]},
    {'method': 'update', 'label': 'California','args': [{'visible': [False, False, False, True, False, False, False, False, False, False, False, False, False]}]}, 
    {'method': 'update', 'label': 'Missouri','args': [{'visible': [False, False, False, False, True, False, False, False, False, False, False, False, False]}]}, 
    {'method': 'update', 'label': 'New Jersey','args': [{'visible': [False, False, False, False, False, True, False, False, False, False, False, False, False]}]},
    {'method': 'update', 'label': 'Montana','args': [{'visible': [False, False, False, False, False, False, True, False, False, False, False, False, False]}]}, 
    {'method': 'update', 'label': 'Washington','args': [{'visible': [False, False, False, False, False, False, False, True, False, False, False, False, False]}]}, 
    {'method': 'update', 'label': 'Illinois','args': [{'visible': [False, False, False, False, False, False, False, False, True, False, False, False, False]}]}, 
    {'method': 'update', 'label': 'North Carolina','args': [{'visible': [False, False, False, False, False, False, False, False, False, True, False, False, False]}]}, 
    {'method': 'update', 'label': 'Oregon','args': [{'visible': [False, False, False, False, False, False, False, False, False, False, True, False, False]}]}, 
    {'method': 'update', 'label': 'Wisconsin','args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, True]}]}]

fig2.update_layout({'updatemenus':[{'type': 'dropdown', 'buttons': dropdown_buttons}]})


fig2.update_layout({'xaxis':{'title':{'text': 'Waarom  Op Lijst'}},
                   'yaxis':{'title':{'text':'Dagen Gezocht'}},
                   'title':{'text':'Aantal Dagen Gezocht per Staat', 'x':0.5}})

fig2.update_layout(updatemenus=[go.layout.Updatemenu(buttons=dropdown_buttons, x = -0.35, xanchor = 'left', 
                                                    y = 1.2, yanchor = 'top',)])

st.plotly_chart(fig2)


# #### ---

# In[18]:


''


# In[19]:


st.subheader('3. Slider')
'Een slider heeft de functie om op een bepaalde variabele geselecteerde waardes weer te geven. De slider in onderstaande grafiek geeft per geselecteerd jaar aan in welke staat het heeft plaatsgevonden en wat voor misdaad of ongeval zich daar heeft afgespeeld.'


# In[20]:


#Sliders
df['Publication Date'] = df['Publication Date'].apply(lambda x: x.split('-')[0])
fig3 = go.Figure()

for x in list(df['Publication Date'].unique()):
    df11 = df[df['Publication Date'] == x]
    fig3.add_trace(go.Scatter(x=df11['State'], y=df11['Why on List'], mode='markers', name=x))
    
sliders = [
    {'steps':[
    {'method': 'update', 'label': '2010','args': [{'visible': [False, False, False, True]}]}, 
    {'method': 'update', 'label': '2018','args': [{'visible': [False, True, False, False]}]}, 
    {'method': 'update', 'label': '2019','args': [{'visible': [False, False, True, False]}]}, 
    {'method': 'update', 'label': '2021','args': [{'visible': [True, False, False, False]}]}]}] 

fig3.update_layout(sliders=sliders)
    
fig3.update_traces(marker=dict(size=10, line=dict(width=2)))   
 
fig3['layout']['sliders'][0]['pad']=dict(r= 10, t= 100,)    

fig3.update_layout({'xaxis':{'title':{'text': 'Staat'}},
                   'yaxis':{'title':{'text':'Waarom op Lijst'}},
                   'title':{'text':'Waarom op Lijst per Staat op Jaar', 'x':0.8}})   

st.plotly_chart(fig3)


# #### ---

# In[21]:


''


# In[22]:


st.subheader('Conclusie')
'Uit de verschillende analyses en verbanden die onderzocht zijn kan eigenlijk geen conclusie getrokken worden. Voordat gestart werd aan dit onderzoek werd verwacht dat er verbanden konden zijn tussen de reward en de tijd dat een persoon op de lijst staat. Echter zit hier helaas geen verband in. Bij het maken van de visualisaties zijn ook geen verbanden gevonden. Zo zit er geen verband in wat voor misdaad per staat heeft plaatsgevonden of tussen de misdaad en de tijd op de lijst. In de tweede grafiek is wel te zien dat voor een misdaad zoals moord of kidnapping mensen langer op de lijst staan. Dit kan dan komen omdat deze mensen gevlucht zijn, aangezien er een hoge straf op ze staat te wachten. De FBI blijft natuurlijk doorzoeken omdat dit ernstige misdrijven zijn. Door het gebrek aan data kunnen we deze conclusie echter niet bevestigen omdat we niet weten of er een relatie zit of dat dit toeval is.'

