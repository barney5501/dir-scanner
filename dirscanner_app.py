import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    file_tree = pd.read_csv("root.csv")[["filename", "parent", "type", "size"]]
    return file_tree


def main():
    print("run!")
    st.title("Dir_ Mapper")
    st.write("Explore your folders")

    file_tree = load_data()
    if "root_folder" not in st.session_state:
        st.session_state.root_folder = file_tree.iloc[-1]["filename"]
        st.session_state.breadcrumbs = [st.session_state.root_folder]
    if "current_dir" not in st.session_state:
        st.session_state.current_dir = st.session_state.root_folder

    # filter to current folder
    current_file_tree = file_tree.loc[
        file_tree["parent"] == st.session_state.current_dir
    ]

    # Breadcrumbs > > >
    st.text(" > ".join(st.session_state.breadcrumbs))

    # Chart
    st.bar_chart(
        data=current_file_tree, x="filename", y="size", horizontal=True, height=500
    )

    # Selectbox for drilldown
    option = st.selectbox(
        "subfolder",
        current_file_tree.loc[current_file_tree["type"] == "folder"],
        index=None,
        placeholder="Select subfolder",
    )

    # Action for select box
    if option:
        st.session_state.current_dir = option
        if option not in st.session_state.breadcrumbs:
            st.session_state.breadcrumbs.append(option)

    # Action for return button (last folder)
    if st.button("back"):
        print(st.session_state.breadcrumbs)

        # st.session_state.breadcrumbs = st.session_state.breadcrumbs[:-1]
        # st.session_state.current_dir = st.session_state.breadcrumbs[-2]
        # print(st.session_state.breadcrumbs)


if __name__ == "__main__":
    main()
