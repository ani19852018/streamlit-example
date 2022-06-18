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
    open = st.sidebar.number_input('open', 50,1000000000000, 926.10,step=1e-6 )
    high = st.sidebar.number_input('high', 50,1000000000000, 931.0 )
    low = st.sidebar.number_input('low', 50,1000000000000, 923.5,step=1e-6 )
    close = st.sidebar.number_input('close', 50,1000000000000, 928.55,step=1e-6 )
    qty = st.sidebar.number_input('qty', 50,1000000000000, 4035417.0 ,step=1e-6)
    turn = st.sidebar.number_input('turn', 50,1000000000000, 3742538282.0 ,step=1e-6)
    notrade = st.sidebar.number_input('notrade', 50,1000000000000, 71254.0 ,step=1e-6)
    delivqty = st.sidebar.number_input('delivqty', 50,1000000000000, 2338783.0 ,step=1e-6)
    percdelqty = st.sidebar.number_input('percdelqty', 1,1000000000000, 57.96,step=1e-6 )
    tempmax = st.sidebar.number_input('tempmax', 5,1000000000000, 25.10,step=1e-6 )
    tempmin = st.sidebar.number_input('tempmin', 5,1000000000000, 13.0)
    temp = st.sidebar.number_input('temp', 5,1000000000000, 19.20,step=1e-6 )
    feelmax = st.sidebar.number_input('feelmax', 5,1000000000000, 25.10,step=1e-6)
    feelmin = st.sidebar.number_input('feelmin', 5,1000000000000, 13.00,step=1e-6 )
    feel = st.sidebar.number_input('feel', 5,1000000000000, 19.20,step=1e-6 )
    dew = st.sidebar.number_input('dew', 5,1000000000000, 9.90,step=1e-6 )
    humid = st.sidebar.number_input('humid', 50,1000000000000, 58.50,step=1e-6 )
    wind = st.sidebar.number_input('wind', 1,1000000000000, 18.10,step=1e-6 )
    winddir = st.sidebar.number_input('winddir', 1,1000000000000, 85.40 ,step=1e-6)
    cloud = st.sidebar.number_input('cloud', 1,1000000000000, 9.50 ,step=1e-6)
    visi = st.sidebar.number_input('visi', 1,1000000000000, 6.30,step=1e-6 )
    solrat = st.sidebar.number_input('solrat', 50,1000000000000, 246.70,step=1e-6 )
    solen = st.sidebar.number_input('solen', 1,1000000000000, 21.50,step=1e-6 )
    uv = st.sidebar.number_input('uv', 1,1000000000000, 9.00,step=1e-6 )
    moonage = st.sidebar.number_input('moonage', 1,1000000000000, 21.00,step=1e-6 )
    rah = st.sidebar.number_input('rah', 1,1000000000000, 15.00,step=1e-6 )
    ram = st.sidebar.number_input('ram', 1,1000000000000, 4.00,step=1e-6 )
    ras = st.sidebar.number_input('ras', 1,1000000000000, 15.00,step=1e-6 )
    decm = st.sidebar.number_input('decm', 1,1000000000000, 27.00 ,step=1e-6)
    decs = st.sidebar.number_input('decs', 1,1000000000000, 2.00,step=1e-6 )
    rise = st.sidebar.number_input('rise', 50,1000000000000, 248.0 )
    cul = st.sidebar.number_input('cul', 50,1000000000000, 814.0 )
    set = st.sidebar.number_input('set', 50,101000000000000000, 1340.0,step=1e-6 )
    appmag = st.sidebar.number_input('appmag', 1,1000000000000, 1.4 ,step=1e-6)
    phase = st.sidebar.number_input('phase', 1,1000000000000, 92.70, step=1e-6)
    earthdist = st.sidebar.number_input('earthdist', 1,1000000000000, 1.89,step=1e-6 )
    sundist = st.sidebar.number_input('sundist', 1,1000000000000, 1.63,step=1e-6 )
    angdiam = st.sidebar.number_input('angdiam', 1,1000000000000, 4.9,step=1e-6 )
    solarsepde = st.sidebar.number_input('solarsepde', 1,1000000000000, 59.1 ,step=1e-6)
    const = st.sidebar.number_input('const', 1,1000000000000, 10.0 )


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
