import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/OmIImO05/arcgeo_template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://cdn.dribbble.com/users/282075/screenshots/2669824/media/3d6b4f00f002736d03d0fb2fae793d84.gif"
st.sidebar.image(logo)


st.title("Searching Basemaps")
st.markdown(
    """
This app is a demonstration of searching and loading basemaps from [xyzservices](https://github.com/geopandas/xyzservices) and [Quick Map Services (QMS)](https://github.com/nextgis/quickmapservices). Selecting from 1000+ basemaps with a few clicks.
"""
)

with st.expander("See demo"):
    st.image("https://i.imgur.com/0SkUhZh.gif")

row1_col1, row1_col2 = st.columns([3, 1])
width = None
height = 800
tiles = None

with row1_col2:

    checkbox = st.checkbox("Search Quick Map Services (QMS)")
    url_input = st.text_input("Enter a URL to load the map:")

    if url_input:
        try:
            m = leafmap.Map()
            m.add_tile_layer(url_input, name="Custom Basemap")
            st.write(m)
        except Exception as e:
            st.error("Error loading the map. Please check the URL.")
            
    empty = st.empty()
    keyword = st.text_input("Enter a keyword to search and press Enter:")
    if keyword is not None:
        keyword = keyword.strip()   
        if keyword:
            options = leafmap.search_xyz_services(keyword=keyword)
            if checkbox:
                options = options + leafmap.search_qms(keyword=keyword)

            tiles = empty.multiselect("Select XYZ tiles to add to the map:", options)



    with row1_col1:
        m = leafmap.Map()

        if tiles is not None:
            for tile in tiles:
                m.add_xyz_service(tile)

        m.to_streamlit(width, height)
