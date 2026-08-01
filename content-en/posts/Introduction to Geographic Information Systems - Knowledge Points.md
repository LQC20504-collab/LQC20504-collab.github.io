---
title: "Introduction to Geographic Information Systems - Knowledge Points"
description: "Knowledge Points Summary"
date: 2026-08-01
tags: ["Knowledge Points"]
---

# Chapter 1 Introduction

- Data
    - Data are direct or indirect original records that describe things and the environment **qualitatively or quantitatively** during human understanding and transformation of the world. They are **unprocessed** raw materials and **representations of objective objects**.
- Information
    - Information is the **content, quantity, or characteristics** of **events, objects, and phenomena** expressed through media such as **text, numbers, symbols, language, and images**. It provides people (or systems) with new **facts and knowledge** about the real world, serving as the **basis** for production, construction, operation, management, analysis, and decision‑making.
- Geographic Information
    - Geographic information is the characterization and all useful knowledge of the properties, characteristics, and states of motion of **geographic entities and phenomena**. It is an **interpretation** of geographic data that expresses the relationships among **geographic features and phenomena**.
- Geographic Data
    - Geographic data are characterized by **spatial distribution, temporal sequencing, massive volume, carrier diversity, and correspondence between location and attributes**.
- Characteristics of Geographic Information
    - Spatial correlation
    - Spatial regionality
    - Spatial diversity
    - Spatial hierarchy
- Geographic Information System (GIS)
    - GIS is a specific and very important spatial information system. It is a technical system that, supported by **computer hardware and software**, performs **collection, storage, management, computation, analysis, display, and description** of relevant **geographic distribution data** for the whole or part of the **Earth's surface** (including the atmosphere).
- Components of GIS
    - Hardware System
        - Input devices
        - Processing devices
        - Storage devices
        - Output devices
    - Software System
        - GIS support software
        - GIS platform software
        - GIS application software
    - Spatial Data
        - Location in a known coordinate system
        - Spatial correlations among entities
        - Attributes unrelated to geometric position
    - Geo‑models
    - Application personnel
- Basic Functions of GIS
    - Data acquisition
    - Data editing and processing
    - Data storage, organization, and management
    - Spatial query and spatial analysis
    - Data output and visualisation
    - Application modelling and system development
- Differences and Connections with Other Information Systems
    - GIS vs. Computer‑Aided Cartography
        - Spatial analysis
    - GIS vs. Database Management Systems
        - Spatial data acquisition, management, and visualisation
    - GIS vs. CAD
        - Spatial analysis
    - GIS vs. Remote Sensing Image Processing Systems
        - Spatial relationships
- Development History of GIS
    - 1960s
    - 1970s
        - In China

# Chapter 2 Mathematical Foundations for Geospatial Science

- Geoid
    - The geoid is a **continuous, closed** equipotential surface that is **everywhere perpendicular** to the direction of gravity. It is assumed to be the surface of the ocean when seawater is in complete static equilibrium, extending beneath all continents from sea level.
- Earth Ellipsoid
    - It is a **regular mathematical surface**. In geodesy and GIS applications, a rotational ellipsoid is generally chosen as an ideal model of the Earth, called the Earth ellipsoid.
- Elevation
    - Elevation is the distance from **a point on the Earth to a reference surface**. For any location, it is as indispensable as the **horizontal measure**.
- Vertical Datum
    - A vertical datum is the starting reference for calculating all **levelling elevations** in a **national unified elevation control network**. It consists of a **levelling base surface** and a **permanent levelling origin**.
    - Major vertical datums in China
        - 1956 Yellow Sea Elevation System
        - 1985 National Elevation Datum
- Map Projection
    - In cartography, map projection is essentially the transformation of the **latitude‑longitude grid** from the Earth's ellipsoid onto a plane according to certain **mathematical rules**. It establishes a **one‑to‑one functional relationship** between the **geographic coordinates** (B, L) of ground points and their corresponding **plane rectangular coordinates** (X, Y) on the map.
    - Classification of Map Projections
        - By construction method
            - Geometric projections
                - By type of auxiliary projection surface
                    - Azimuthal projection
                    - Cylindrical projection
                    - Conic projection
                - By orientation of the projection surface relative to the Earth's rotation axis
                    - Normal (direct) projection
                    - Transverse projection
                    - Oblique projection
                - By position relative to the Earth
                    - Secant projection
                    - Tangent projection
            - Non‑geometric projections
                - Pseudo‑azimuthal projection
                - Pseudo‑cylindrical projection
                - Pseudo‑conic projection
                - Polyconic projection
        - By distortion property
            - Conformal projection
            - Equal‑area projection
            - Arbitrary and equidistant projections
    - Common Map Projections
        - Gauss‑Krüger projection
            - Transverse conformal tangent cylindrical projection
            - The central meridian and the equator are perpendicular straight lines; other meridians are concave curves symmetric about the central meridian; other parallels are curves symmetric about the equator and curving toward the poles.
            - Along the same meridian, length distortion increases as latitude decreases, reaching a maximum at the equator; along the same parallel, length distortion increases rapidly with increasing longitude difference.
            - It is an internationally used projection suitable for large countries or regions.
        - Universal Transverse Mercator (UTM) projection
            - Transverse conformal secant cylindrical projection
            - Mainly used for mapping areas between 84°N and 80°S globally.
        - Lambert conformal conic projection
            - Normal conformal secant conic projection
            - Parallels are concentric arcs, meridians are radii of the concentric circles.
    - Selection of Map Projections
        - Extent of the mapping area
        - Shape and geographic location
        - Purpose of the map
        - Publication method and other special requirements
- Spatial Coordinate Transformation
    - Spatial coordinate transformation maps **spatial data** from one **spatial reference system** to another.
    - Also sometimes called projection transformation.
    - Methods
        - Direct transformation
        - Inverse transformation
        - Numerical transformation
- Scale
    - Specifically refers to the **ratio of map length to ground length**.
- Resolution
    - Image resolution is simply a measure of **the ability to resolve details in imaging**, and also an indicator of the **fineness of objects** in the image, representing the **level of detail of scene information**.
    - Spectral resolution
    - Temporal resolution
    - Spatial resolution

# Chapter 3 Spatial Data Models

- Geographic Space
    - In geography, geographic space refers to the **Earth's surface and near‑surface space**, which is the region of **interaction** among the atmosphere, hydrosphere, biosphere, lithosphere, and pedosphere. The most complex physical, chemical, biological, and biogeochemical processes on Earth occur in this region.
- Conceptual Models
    - A conceptual model is an **abstract set of concepts** for geographic objects and phenomena in geographic space, and it is the **semantic interpretation** of geographic data. From a computer system perspective, it is the **highest level of system abstraction**.
    - According to GIS data organisation and processing methods, the main conceptual models for geospatial data currently include:
        - Object model (feature model)
            - The object data model (also called feature model) treats the entire geographic space as a **domain** in which geographic phenomena and spatial entities are distributed as **independent objects**.
        - Field model
            - The field data model (also called domain model) treats geographic phenomena as **continuous variables or bodies**, such as air pollution levels, surface temperature, etc.
        - Network model
        - Spatio‑temporal model
        - Multi‑dimensional model
- Representation of Logical Models
    - Standard logical model design is usually expressed using entity‑relationship diagrams.
        - E‑R diagram
- Spatial Data Types
    - Geometric data
    - Raster (pixel) data
    - Attribute data
    - Metadata
- Representation of Geometric Data
    - Point
    - Line
    - Polygon (area)
    - Volume (body)
- Spatial Resolution of Imagery
    - Spatial resolution of imagery refers to the **size of the ground area** represented by a **single pixel** in terms of **side length**. The higher the spatial resolution (smaller value), the smaller the ground area per pixel, and thus the higher the level of detail. This is the opposite of scale, where a smaller scale shows less detail.
- Spatial Relationships
    - Spatial relationships refer to the interactions **among geographic spatial entities**.
        - Topological spatial relationships
            - Topological relationships on maps are properties that remain **unchanged under continuous deformations** (such as scaling, rotation, and stretching) of the graphics, i.e., **graphical relationships remain invariant**.
                - Adjacency
                - Association
                - Containment
                - Connectivity
            - They are of great significance for data processing and spatial analysis
                - Topological relationships clearly reflect the **logical structural relationships among entities**; they are more stable than geometric coordinate relationships and do not change with projection transformations.
                - They facilitate **spatial feature queries**.
                - They allow **reconstruction of geographic entities** based on topological relationships.
        - Order (sequential) spatial relationships
        - Metric spatial relationships
- Characteristics and Representation of Imagery Data
    - Pixel value assignment methods
        - Centre‑point method
        - Area‑dominant method
        - Importance method
        - Length‑dominant method

# Chapter 4 Spatial Data Structures

- Vector Data Structure
    - A vector data structure organises data according to the **vector data model**, using points, lines, and polygons (and their combinations) from Euclidean geometry to represent the **spatial distribution of geographic entities**.
    - It is divided into entity data structure and topological data structure, depending on whether spatial relationships among geographic entities are explicitly represented.
        - Entity data structure (Spaghetti structure)
            - The entity data structure, also called Spaghetti data structure, organises **line segments** that form **polygon boundaries** by **polygon** as the unit.
        - Topological data structure
            - Vector data structures that contain topological relationships are called topological data structures. Their common feature is that points are independent, points connect to form lines, and lines form polygons. Each line starts at a **start node** and ends at an **end node**, and is adjacent to left and right polygons.
            - Includes:
                - Indexed structure
                - Dual independent map encoding (DIME)
                - Chain‑node topological structure (e.g., POLYVRT)
    - It has the characteristic of “**explicit location, implicit attributes**”.
- Raster Data Structure
    - A raster data structure represents spatial objects using a **regular grid array**. The value in each grid cell represents the **attribute characteristics** of the spatial object.
    - It has the characteristic of “**explicit attributes, implicit location**”.
- Compressed Raster Data Structures
    - Run‑length encoding
    - Quadtree data structure
    - Two‑dimensional run‑length encoding
- Imagery and Tile Pyramid Data Structure
    - The imagery pyramid data structure stores and displays data at **different spatial resolutions** within a **unified spatial reference** according to user needs, forming a pyramid with **resolution gradually increasing from coarse to fine and data volume from small to large**.
- Comparison of Raster and Vector Data Structures
    - Vector Data Structure
        - Advantages
            - Compact data structure, low **redundancy**, small data volume.
            - Clear **topological relationships**, easy for network analysis.
            - Object‑oriented, not only expresses attribute codes but also conveniently records detailed **attribute descriptions** for each object.
            - Supports **graphic data** recovery, updating, and generalisation.
            - High **display** quality and accuracy.
        - Disadvantages
            - Complex **algorithms** for data processing.
            - Overlay analysis and **combination** with raster maps are difficult.
            - **Mathematical modelling** is relatively difficult.
            - **Spatial analysis techniques** are more complex and require more sophisticated hardware and software.
            - **Display and plotting costs** are relatively high.
    - Raster Data Structure
        - Advantages
            - **Simple** data structure, easy to implement algorithms.
            - **Overlay and combination** of spatial data are easy, facilitating matching and analysis with remote sensing data.
            - Various **spatial analyses and geographic phenomenon simulations** are relatively easy.
            - **Output methods** are fast, simple, and low‑cost.
        - Disadvantages
            - Large **data volume**; reducing data volume by using larger pixels leads to **loss** of accuracy and information.
            - Difficult to establish **spatial network** connectivity.
            - **Projection transformation** is difficult to implement.
            - Lower graphic data quality, map output is **less refined**.

# Chapter 5 Spatial Data Organisation and Management

- Spatial Database
    - A GIS database (spatial database or geodatabase) is a collection of data about the **characteristics of geographic features** within a certain region.
    - Compared with general databases, it has the following characteristics:
        - Extremely large data volume
        - Complex data structures
        - Diverse data relationships
        - Wide range of applications
- Management of Vector Data
    - File‑relational database hybrid management
    - Full relational database management
    - Object‑relational database management
- Index
    - An index is a **quick data retrieval** mechanism in a database, usually consisting of **keywords and storage addresses**.
- Spatial Index
    - A spatial index is a data structure that arranges spatial objects according to their **location and shape** or **certain spatial relationships** in a given **order**. It contains **summary information** about the spatial objects, such as object identifiers, bounding rectangles, and pointers to the actual spatial entities.
- Spatial Indexing Algorithms
    - Object‑range index
        - When recording the **coordinates** of each spatial entity, the **minimum and maximum coordinates** of its **bounding rectangle** are also recorded. This method does not create a **dedicated spatial index file**; instead, the **min‑max ranges** are added to the spatial object data file, and discrimination relies mainly on **spatial calculations**.
    - Grid‑based spatial index
        - The entire study area is divided into **equal‑sized grid cells** according to certain rules, and the **spatial entities** contained in each grid cell are recorded. To facilitate building a **linear table** for the spatial index, each grid cell is encoded using a **Morton code**, and the relationship between Morton codes and spatial entities is established as the **grid index file**.
    - Quadtree spatial index
        - When building a quadtree index, the **extent** covered by all spatial objects is used to perform **quadtree partitioning** so that each sub‑block contains a **single entity**. An **index** is then built based on the **level** or **size** of the sub‑block containing each entity.
    - R‑tree index
        - The R‑tree spatial index not only uses the bounding rectangles of individual entities but also groups the bounding rectangles of **spatially proximate** entities into a **larger virtual rectangle**. These virtual rectangles are then indexed, with pointers to the **spatial entities they enclose**.

# Chapter 6 Spatial Data Acquisition and Processing

- Classification of Data Sources
    - By acquisition method:
        - Map data
        - Remote sensing imagery
        - Field survey data
        - Shared data
        - Other data
    - By data form:
        - Digital data
        - Multimedia data
        - Textual data
- General Workflow of Spatial Data Acquisition and Processing
    - Selection of data sources
    - Determination of acquisition methods
    - Data editing and processing
    - Data quality control and evaluation
    - Data loading into database
- Methods of Spatial Data Acquisition
    - Mainly include:
        - Field data collection
        - Digitisation of existing maps
        - Photogrammetric methods
        - Remote sensing image processing methods
- Coordinate Transformation
    - To unify data into the **same spatial reference system**. The essence of coordinate transformation is to establish a **one‑to‑one correspondence of points between two spatial reference systems**.
    - Common coordinate transformation methods:
        - Projection transformation
        - Affine transformation
        - Similarity transformation
        - Rubber‑sheeting
- Resampling
    - Resampling is a common data processing method used in raster data spatial analysis to handle **raster resolution matching** problems.
    - Common resampling methods:
        - Nearest neighbour
        - Bilinear interpolation
        - Bicubic convolution
- Common Polygon Filling Algorithms
    - Internal point diffusion method
    - Ray casting method
    - Scan‑line method
- Vector Data Compression
    - The purpose is to **remove redundant data**, reduce **storage volume**, save **storage space**, and accelerate **subsequent processing**.
        - Common compression methods:
            - Point‑interval sampling
            - Perpendicular distance and angle method
            - Split (Douglas‑Peucker) method
- Errors in Spatial Data
    - Random errors
    - Systematic errors
    - Gross errors (blunders)
- Metadata
    - Metadata is **data about data**.
    - Main functions:
        - Help users understand and analyse data
        - Spatial data quality control
        - Application in data integration
        - Data storage and function implementation

# Chapter 7 Basic Spatial Analysis in GIS

- Spatial Analysis
    - Spatial analysis is an **analytical technique** that, supported by **a series of spatial algorithms** and based on **geoscience principles**, obtains information about the spatial location, morphology, distribution, relationships, and evolution of geographic phenomena or entities according to their **distribution characteristics** in space, and performs simulation, interpretation, and prediction.
- Types of Spatial Analysis
    - By data model:
        - Field‑based spatial analysis
        - Object‑based spatial analysis
        - Network‑based spatial analysis
        - Spatio‑temporal model‑based spatial analysis
    - By data dimension:
        - 2D spatial analysis
        - 2.5D spatial analysis
        - Multi‑dimensional spatial analysis
    - By analytical level:
        - Basic spatial analysis methods
        - Spatial statistical analysis
        - Intelligent spatial analysis methods
- Basic Measurement Methods for Spatial Objects
    - Geometric measurement
    - Distance measurement
    - Angle measurement
- Overlay Analysis
    - Overlay analysis superimposes **various thematic data layers** to produce a new data layer. The result combines the **attributes** of the original layers, generates new **spatial relationships**, and also links the attributes of the input layers to create new **attribute relationships**.
    - By operation form:
        - Erase
        - Intersect
        - Union (merge)
    - By element type:
        - Vector overlay analysis
            - Point‑in‑polygon overlay
            - Line‑in‑polygon overlay
            - Polygon‑on‑polygon overlay
        - Raster overlay analysis
            - Single‑layer raster overlay
            - Multi‑layer raster overlay
- Raster Overlay Operation Methods
    - Boolean logic operations
    - Reclassification
    - Mathematical combination (composite) operations
- Buffer
    - A buffer is a representation of the **influence zone** or **service area** of a geographic spatial object at a given **scale**.
- Buffer Analysis
    - Buffer analysis automatically creates a buffer zone of a certain width around point, line, or polygon entities **based on the database**, thereby extending spatial data in the **horizontal direction** for **information analysis**.
- Types of Vector Buffers
    - By object type:
        - Point buffer
        - Line buffer
        - Polygon buffer
- Construction of Vector Buffers
    - Two most common methods:
        - Angle bisector method
        - Convex corner arc method
- Window Analysis
    - Window analysis is a technique for **raster data systems** that opens an analysis window with a **fixed radius** around one or more raster cells (or the entire dataset), performs **statistical calculations** such as extrema, mean, etc., within the window, and/or conducts **composite analysis** with other layers, thus effectively realising **horizontal expansion analysis** of raster data.
    - Three elements of window analysis:
        - Centre point
        - Size and type of the analysis window
        - Operation mode
    - Types of analysis windows:
        - Rectangular window
        - Circular window
        - Annular (ring) window
        - Sector window
        - Other windows
- Network Analysis
    - Network analysis is a field that studies **network status** and the **flow and allocation of resources** on networks through simulation and analysis, addressing **optimisation problems** related to network structure, flow efficiency, and network resources.
- Attributes in Vector Networks
    - Impedance
    - Resource capacity
    - Resource demand

# Chapter 8 DEM and Digital Terrain Analysis

- Digital Elevation Model (DEM)
    - A DEM is a **digital simulation** of a **terrain surface** using **limited terrain elevation data**. It represents the **model‑based expression** and **process simulation** of geographic phenomena that exhibit **continuous variation** over two‑dimensional geographic space.
- Digital Terrain Analysis (DTA)
    - DTA refers to digital information processing techniques that perform **attribute calculations** and **feature extraction** on a **DEM**.
    - Common methods of digital terrain analysis:
        - Extraction of slope‑related terrain factors
        - Extraction of characteristic terrain features
        - Statistical analysis of terrain characteristics
    - Basic terrain factor analysis:
        - Slope
        - Aspect
        - Curvature
        - Macro‑terrain factors
    - Terrain feature analysis:
        - Extraction of terrain feature points
        - Extraction of ridge lines and valley lines
    - Watershed analysis
    - Visibility analysis
        - Visibility analysis, also called **intervisibility analysis**, essentially falls under **optimisation processing** of terrain.
        - The two basic factors of visibility analysis are **intervisibility between two points** and the **viewshed**, i.e., the area covered from a given observation point.
- DEM Interpolation Methods
    - By the spatial extent of interpolation points:
        - Global interpolation
        - Local interpolation
        - Point‑by‑point interpolation

# Chapter 9 Spatial Statistical Analysis

## Spatial Statistical Analysis (p.227)

It can include **statistical analysis of spatial data** and **spatial statistical analysis of data**.

The former focuses on the **non‑spatial characteristics** of spatial objects and phenomena, addressing the main problem of how to use **mathematical statistical models** to describe and simulate spatial phenomena and processes.

The latter directly starts from the spatial positions and relationships of spatial objects, studying natural phenomena that exhibit both **randomness** and **structure**, or **spatial correlation** and **dependence**.

## Classification (Data Classification) (p.243)

It refers to classification according to **fixed schemes**, where the class intervals are automatically determined by **specific algorithms**.

- Equal interval classification
- Quantile classification
- Equal area classification
- Standard deviation classification
- Natural breaks (Jenks) classification
- Other classification methods

# Chapter 10 Geographic Information Visualisation and Cartography

## Visualisation (p.267)

The full name is Scientific Visualisation.

It is the theory, method, and technology that uses **computer graphics and image processing techniques** to convert data into **graphics or images** displayed on a screen, and to perform **interactive processing**.

## Geographic Information Visualisation (p.268)

It applies **graphics, computer graphics, and image processing techniques** to display and interact with the results of **geoinformation** input, processing, query, analysis, and prediction in the form of graphical symbols, icons, text, tables, videos, and other visualisation formats. It is an important component of GIS.

Among them, **map‑based** geographic information visualisation is the core content.

## Virtual Reality (p.300)

Virtual reality is a **computer‑generated** **three‑dimensional virtual environment** integrating visual, auditory, and tactile senses. Users interact with the virtual environment **naturally** using **specific devices**, obtaining experiences that are equivalent to the real world and even those difficult to experience in reality.

## Classification of GIS Output Products (p.271)

- Maps
- Images
- Statistical charts and graphs

## General Arrangement of Map Content (p.284)

### Main Map and Supplementary Maps

In terms of spatial extent, the main map area should be distinguished from neighbouring areas using a figure‑ground relationship, enhancing the visual contrast of the main map region.

The orientation of the main map is conventionally north‑up.

Inset maps (locator maps).

Enlarged maps for important areas.

### Map Title

### Legend

### Scale Bar

### North Arrow (Compass Rose)

### Statistical Charts and Text Descriptions

### Map Neatlines and Reference Grids

## Visualisation Representation Forms (p.288)

- Thematic map display
- Contour (isoline) display
- Hypsometric tinting (layer colouring)
- Hill shading (shaded relief)
- Profile display
- Perspective (3D) display
- 3D landscape visualisation
- Spatio‑temporal data display
- Virtual reality techniques
- 3D dynamic roaming (fly‑through)

## Thematic Mapping Methods

### Point Symbol Method

Uses point symbols of different shapes, sizes, and colours to represent discretely distributed geographic phenomena, with each symbol corresponding to a specific point location.

Symbols can be quantitative (e.g., circle size representing urban population).

Suitable for precise coordinate data (e.g., weather stations, oil fields, cities).

### Line Symbol Method

Uses linear symbols to represent geographic features with linear extension. Types are distinguished by line width, colour, and style (solid, dashed, etc.).

It does not reflect actual width (e.g., the width of a river or road on the map is not the actual width).

Arrows can be added to indicate direction (e.g., ocean currents, wind directions).

### Qualitative Background (Area‑Colour) Method

Uses different colours or textures to fill areas, representing continuously distributed categorical data with no overlap between categories.

Must be complete coverage without gaps (e.g., administrative divisions, geological lithology maps).

The legend must clearly define class boundaries.

### Range Method

Uses area‑based colour patches or patterns to represent discontinuously distributed geographic phenomena, allowing overlapping or blank areas.

Boundaries can be fuzzy (e.g., animal habitats, dialect regions).

Transparency can be overlaid to indicate intensity (e.g., pollution extent).

### Ratio (Density) Method

Converts statistical data into relative values (e.g., density, percentage) and represents them using choropleth maps or dot‑density maps.

Eliminates the influence of area size (e.g., population density vs. total population).

Requires standardised data processing.