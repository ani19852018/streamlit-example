import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
model3 = pickle.load(open('lstm.sav', 'rb'))

st.title('Stock Prediction')
st.sidebar.header('Stock Data')


# FUNCTION
def user_report():
    open = st.sidebar.number_input('open', 50,10000, 100 )
    high = st.sidebar.number_input('high', 50,10000, 100 )
    low = st.sidebar.number_input('low', 50,10000, 100 )
    close = st.sidebar.number_input('close', 50,10000, 100 )
    qty = st.sidebar.number_input('qty', 50,10000000, 100 )
    turn = st.sidebar.number_input('turn', 50,10000, 100 )
    notrade = st.sidebar.number_input('notrade', 50,10000, 100 )
    delivqty = st.sidebar.number_input('delivqty', 50,10000, 100 )
    percdelqty = st.sidebar.number_input('percdelqty', 50,10000000, 100 )
    tempmax = st.sidebar.number_input('tempmax', 50,10000, 100 )
    tempmin = st.sidebar.number_input('tempmin', 50,10000000, 100 )
    temp = st.sidebar.number_input('temp', 50,10000, 100 )
    feelmax = st.sidebar.number_input('feelmax', 50,10000, 100 )
    feelmin = st.sidebar.number_input('feelmin', 50,10000, 100 )
    feel = st.sidebar.number_input('feel', 50,10000, 100 )
    dew = st.sidebar.number_input('dew', 50,10000000, 100 )
    humid = st.sidebar.number_input('humid', 50,10000, 100 )
    wind = st.sidebar.number_input('wind', 50,10000, 100 )
    winddir = st.sidebar.number_input('winddir', 50,10000, 100 )
    cloud = st.sidebar.number_input('cloud', 50,10000, 100 )
    visi = st.sidebar.number_input('visi', 50,10000000, 100 )
    solrat = st.sidebar.number_input('solrat', 50,10000, 100 )
    solen = st.sidebar.number_input('solen', 50,10000, 100 )
    uv = st.sidebar.number_input('uv', 50,10000, 100 )
    moonage = st.sidebar.number_input('moonage', 50,10000, 100 )
    rah = st.sidebar.number_input('rah', 50,10000000, 100 )
    ram = st.sidebar.number_input('ram', 50,10000, 100 )
    ras = st.sidebar.number_input('ras', 50,10000, 100 )
    decm = st.sidebar.number_input('decm', 50,10000, 100 )
    decs = st.sidebar.number_input('decs', 50,10000, 100 )
    rise = st.sidebar.number_input('rise', 50,10000000, 100 )
    cul = st.sidebar.number_input('cul', 50,10000, 100 )
    set = st.sidebar.number_input('set', 50,10000, 100 )
    appmag = st.sidebar.number_input('appmag', 50,10000, 100 )
    phase = st.sidebar.number_input('phase', 50,10000, 100 )
    earthdist = st.sidebar.number_input('earthdist', 50,10000000, 100 )
    sundist = st.sidebar.number_input('sundist', 50,10000, 100 )
    angdiam = st.sidebar.number_input('angdiam', 50,10000, 100 )
    solarsepde = st.sidebar.number_input('solarsepde', 50,10000, 100 )
    const = st.sidebar.number_input('const', 50,10000, 100 )


    user_report_data = {
      'open':open, 'high':high, 'low':low, 'close':close, 'qty':qty, 'turn':turn,
      'notrade':notrade,
      'delivqty':delivqty,
      'percdelqty':percdelqty,
      'tempmax':tempmax,
      'tempmin':tempmin,
      'temp':temp,
      'feelmax':feelmax,
      'feelmin':feelmin,
      'feel':feel,
      'dew':dew,
      'humid':humid,
      'wind':wind,
      'winddir':winddir,
      'cloud':cloud,
      'visi':visi,
      'solrat':solrat,
      'solen':solen,
      'uv':uv,
      'moonage':moonage,
      'rah':rah,
      'ram':ram,
      'ras':ras,
      'decm':decm,
      'decs':decs,
      'rise':rise,
      'cul':cul,
      'set':set,
      'appmag':appmag,
      'phase':phase,
      'earthdist':earthdist,
      'sundist':sundist,
      'angdiam':angdiam,
      'solarsepde':solarsepde,
      'const':const
      }
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data


user_data = user_report()
st.header('Stock Data')
st.write(user_data)

tomclose = model3.predict(user_data)
st.subheader('Tomorrow Close')
st.subheader('Rs'+str(tomclose))
