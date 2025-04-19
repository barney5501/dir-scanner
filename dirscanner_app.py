import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    file_tree = pd.read_csv("root.csv")[["filename", "parent", "type", "size"]]
    return file_tree


def main():
    st.title("Dir_ Mapper")
    st.write("Explore your folders")

    file_tree = load_data()
    if "root_dir" not in st.session_state:
        st.session_state["root_dir"] = file_tree.iloc[-1]["filename"]
        st.session_state["breadcrumbs"] = [st.session_state["root_dir"]]
        st.session_state["current_dir"] = st.session_state["root_dir"]

    # filter to current folder
    current_file_tree: pd.DataFrame = file_tree.loc[
        file_tree["parent"] == st.session_state["current_dir"]
    ].sort_values(by="size")

    # Breadcrumbs > > >
    st.text(" > ".join(st.session_state["breadcrumbs"]))

    # Chart
    st.bar_chart(
        data=current_file_tree,
        x="filename",
        y="size",
        horizontal=True,
        height=500,
    )

    col1_selectbox, col2_button = st.columns(2, vertical_alignment="bottom")

    options = current_file_tree.loc[current_file_tree["type"] == "folder"]["filename"]
    # Selectbox for drilldown
    with col1_selectbox:
        option = st.selectbox(
            "subfolder",
            options=options,
            index=None,
            placeholder="Select subfolder",
        )
    with col2_button:
        st.button("select")
        st.empty()

    # Action for select box
    if option:
        st.session_state["current_dir"] = option
        if option not in st.session_state["breadcrumbs"]:
            st.session_state["breadcrumbs"].append(option)

    # Action for return button (last folder)
    if st.button("back"):
        if st.session_state["current_dir"] != st.session_state["root_dir"]:
            st.session_state["breadcrumbs"] = st.session_state["breadcrumbs"][:-1]
            st.session_state["current_dir"] = st.session_state["breadcrumbs"][-1]
            st.rerun()


if __name__ == "__main__":
    main()
