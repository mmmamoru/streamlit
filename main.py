# main.py
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

def main():
    st.title("title! 超入門")
    st.write(("Hello World!"))

    st.write('プログレスバーの表示')
    'Start!!'

    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    'Done!!'


    left_column, right_column = st.columns(2)

    button = left_column.button('右カラムに文字を表示')
    if button:
        right_column.write('ここは右カラム')

    expander1 = st.expander('問い合わせ1')
    expander1.write('問い合わせ1内容を書く')
    expander2 = st.expander('問い合わせ2')
    expander2.write('問い合わせ2内容を書く')
    expander3 = st.expander('問い合わせ3')
    expander3.write('問い合わせ3内容を書く')


    # text = st.text_input('あなたの趣味を教えてください')
    # condition = st.slider('あなたの今の調子は？', 0, 100, 50)

    # st.write('あなたの趣味: ', text)
    # st.write('あなたの調子は', condition)


    # st.sidebar.write('display image')

    # text = st.sidebar.text_input('あなたの趣味を教えてください')
    # condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

    # st.write('あなたの趣味: ', text)
    # st.write('あなたの調子は', condition)


    # text = st.text_input('あなたの趣味を教えてください')
    # condition = st.slider('あなたの今の調子は？', 0, 100, 50)
    # st.write('あなたの趣味: ', text)
    # st.write('あなたの調子は', condition)


    # option = st.selectbox(
    #     'あなたがすこな数字を教えてください, ',
    #     list(range(1,11))
    # )
    # 'あなたの好きな数字は、', option, 'です。'


#     if st.checkbox('Show image'):
#         img = Image.open('sample.png')
#         st.image(img, caption='sample', use_column_width=True)

    # st.write('Display Image')
    # img = Image.open('sample.png')
    # st.image(img, caption='sample', use_column_width=True)

    # df = pd.DataFrame(
    #     np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
    #     columns=['lat', 'lon'] 
    # )
    # st.map(df)

    # st.bar_chart(df)
    # st.area_chart(df)
    # st.line_chart(df)



    # df = pd.DataFrame({
    #     '1列目': [1,2,3,4],
    #     '2列目': [10,20,30,40]
    # })

    # st.dataframe(df.style.highlight_max(axis=0))
    # st.dataframe(df.style.highlight_max(axis=0))
    # st.table(df.style.highlight_max(axis=0))
    # st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
    # st.write(df)



    # """
    # # 章
    # ## 節
    # ### 項

    # ```python
    # import streamlit as st
    # import numpy as np
    # import pandas as pd
    # ```

    # """




if __name__ == "__main__":
    main()
    
