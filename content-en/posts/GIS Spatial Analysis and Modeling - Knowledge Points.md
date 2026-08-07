---
title: "GIS Spatial Analysis and Modeling - Knowledge Points"
description: "Knowledge Points Summary"
date: 2026-08-07
tags: ["Knowledge Points"]
---

# Introduction to GIS Spatial Analysis

Spatial Analysis
- Spatial analysis is a spatial data analysis technique based on the location and morphological characteristics of geographic objects, with the purpose of extracting and transmitting spatial information.
- Spatial analysis is the main feature of geographic information systems, and also one of the key indicators for evaluating GIS functionality.
- Spatial analysis is the foundation for various comprehensive geoscience analysis models, providing basic methods for building complex spatial application models.

What are the main spatial data models for spatial analysis?
- Classification
  - From the perspective of data structure
    - Vector data model
    - Raster data model
  - Dimensions and other special requirements
    - 3D
    - Spatio-temporal
    - ...

Raster Data Model
- In the raster data model, geographic space is divided into regular units (pixels), and spatial location is represented by row and column numbers of pixels.
- The pixel size reflects the resolution of the data, and spatial objects are implicitly described by a set of pixels.

Vector Data Model
- The vector data model treats geographic space as a spatial region in which geographic features exist.
- In the vector data model, geographic features are classified into points, lines, and polygons according to their spatial morphological characteristics, providing explicit location and implicit attribute descriptions for entities.

Differences and Connections between Vector and Raster Data Models
- The biggest difference between raster and vector data is that the former uses cell space filling to represent collections, while the latter uses point sequences to represent boundary shapes and distributions.
- Therefore, the raster data structure (space-oriented) has obvious advantages in Boolean operations, overall operation feature calculations, and spatial retrieval, while the vector data structure (object-oriented) easily facilitates model generation, object display, and geometric transformations.
- Given the complementary advantages of raster and vector data structures, research on integrated raster-vector data structures has become the foundation for developing a new generation of GIS software.

Raster Data Analysis Modes
- Due to the characteristics of its data structure, raster data typically uses the two-dimensional digital matrix analysis method of linear algebra as the mathematical basis for data processing and analysis, featuring relatively simple automatic analysis and strong patternization.
- Raster data analysis methods can be summarised into several basic analysis modes:
  - Aggregation and cluster analysis
  - Composite analysis
  - Tracking analysis
    - Tracking analysis in raster data systems refers to a spatial analysis method that extracts target or trajectory information by starting from one or more starting points and following certain tracking clues.
  - Window analysis
    - Window analysis opens an analysis window with a fixed radius around one or more raster cells (or the entire dataset), performs statistical operations such as extrema and mean within the window, and/or composite analysis with other layers, thus realising horizontal expansion analysis of raster data.
  - Statistics and measurement

**# Vector Data Analysis Methods**
- Vector data inclusion analysis
- Vector data buffer analysis
  - Buffer
- Polygon overlay analysis
  - Overlay
- Vector data network analysis
- Thiessen polygon analysis
  - This method connects all adjacent meteorological stations to form triangles, then draws the perpendicular bisectors of each side of these triangles. The several perpendicular bisectors around each station enclose a polygon.
  - The rainfall intensity of the unique meteorological station contained within this polygon is used to represent the precipitation intensity of this polygonal area, and this polygon is called a Thiessen polygon.
- Vector data measurement

The spatial analysis functions of ArcGIS 10 mainly include:
- Spatial Analyst module
- 3D Analyst module
- Geostatistical Analyst module
- Temporal Analyst module
- Network Analyst module
- Tracking Analyst module

# Vector Data Spatial Analysis

Buffer
- A buffer is an information analysis method that creates polygon entities with a certain range around a set or class of map features (points, lines, or polygons) according to set distance conditions, thereby realising two-dimensional spatial expansion of data.
- The forms of buffers are diverse, mainly determined by the conditions for establishing the buffer.
  - Point buffer
    - Circular
    - Annular
  - Line buffer
    - Symmetrical on both sides
    - Asymmetrical on both sides
    - Single-sided buffer
  - Polygon buffer
    - Inner buffer
    - Outer buffer

Overlay Analysis
- Overlay analysis superimposes various data layers representing different themes to produce a new data layer, and the overlay result combines the attributes of the original two or more layers.
- (Briefly describe three or more overlay analysis methods) Can be divided into:
  - Spatial Join
    - Connects attributes from one feature class to another based on spatial relationships.
  - Erase
    - Erases features in the input layer that are covered by the erase reference layer according to its extent.
  - Identity
    - In identity overlay, the attributes of the identity layer are assigned to the map features of the input layer in the overlapping areas; sometimes the overlapping areas also undergo partial geometric changes.
  - Intersect
    - Obtains the intersection of two layers through overlay processing, and all attributes of the original layers are displayed on the new layer.
  - Symmetrical Difference
    - In vector overlay analysis, sometimes only the remaining parts after removing the common area of two layers are needed. The attributes of the new layer are also generated by combining the attributes of both layers.
  - Union
    - Combines the extents of the two layers while retaining all features from both the input and overlay layers.
  - Update
    - First performs a geometric intersection between the input layer and the update layer, then the attributes of the input layer that are covered by the update layer are replaced by the attributes of the update layer. When both layers are polygon features, they are merged.
  - Split and Clip (Clip is in the Extraction toolbox, others are in the Overlay toolbox)

Network Analysis
- Network analysis is the process of geographic analysis and modeling of geographic networks (e.g., transportation networks) and urban infrastructure networks (e.g., various cables, power lines, telephone lines, water supply lines, drainage pipes, etc.). By studying the state of networks and simulating and analysing the flow and distribution of resources on networks, it solves optimisation problems related to network structure and resources.
- Transportation Network Analysis
  - Overview
    - Transportation network analysis is commonly used for road, subway, and other transportation networks, studying routes, service areas, and resource allocation.
    - In transportation network analysis, two-way travel is allowed on network edges, and agents in the network have the ability to choose directions subjectively.
  - Applications
    - The main problems it can solve include:
      - Calculating the best path between points, freely adjusting the order of points
      - Finding the nearest one or more facility points
      - Determining the service area of one or more facility points
      - Creating origin-destination cost matrices
      - Vehicle routing problem (VRP)
- Utility Network Analysis
  - Overview
    - Mainly used for river network analysis and utility network analysis, studying the state of networks and simulating and analysing the flow and distribution of resources on networks.
    - Only one-way travel is allowed on network edges, and agents in the network cannot choose their direction of travel; their paths are determined by external factors.
  - Applications
    - The main problems it can solve include:
      - Finding connected/disconnected pipelines
      - Upstream/downstream tracing
      - Finding loops
      - Finding paths
      - Pipe burst analysis
      ![image-1](/images/gis-knowledge/mubu-01.jpg)

# Raster Data Spatial Analysis

Main Analysis Tools
- Distance mapping
- Density mapping
- Surface analysis
- Raster calculator
- Reclassification
- Statistical analysis
- Multivariate analysis

What are the spatial analysis modules in ArcGIS?

Distance Mapping Analysis
- Distance mapping analysis creates maps based on the distance from each raster cell to its nearest feature (also called "source"), reflecting the relationship between each raster cell and its nearest source.
- Basic idea of shortest path finding
  - Shortest path finding first requires obtaining cost data.
  - Then execute a cost-weighted distance function to obtain cost direction data and cost distance data from the origin.
  - Finally, execute the shortest path function to obtain the shortest or optimal path from the origin to the destination.

Density Mapping Analysis
- Density mapping calculates the data aggregation status of the entire area based on the input feature dataset, generating a continuous density surface.

Surface Analysis
- Surface analysis mainly generates new datasets, such as contours, slope, aspect, hillshade, and other derived data, to obtain more information about spatial characteristics, patterns, etc., hidden in the original dataset.
- Main functions of surface analysis in ArcGIS
  - In ArcGIS, the main functions of surface analysis include:
    - Querying surface values
    - Deriving slope and aspect information from the surface
      - Slope
        - The slope at any point on a terrain surface is the angle between the tangent plane at that point and the horizontal plane. Slope represents the degree of inclination of the surface at that point.
      - Aspect
        - Aspect refers to the angle between the projection of the normal vector of the tangent plane at a point on the terrain surface onto the horizontal plane and the true north direction through that point. For any point on the ground, aspect indicates the direction of the maximum change in elevation value.
    - Creating contours
      - Contour
        - Contours are lines connecting adjacent points on a surface that have the same value, such as contour lines on topographic maps or isotherms on temperature maps.
    - Analysing surface visibility
    - Calculating hillshade from the surface
      - Hillshade
        - Hillshade calculates the illumination value for each raster cell of an elevation raster grid based on a hypothetical illumination source.

What are the mathematical operators?
- Arithmetic operators
- Boolean operators
- Relational operators

Reclassification
- Reclassification is the process of reassigning new values to original values, resulting in a new set of output values.
- Basic classification forms:
  - New value replacement
  - Setting null values
  - Merging old values
  - Reclassifying

Three common statistical analysis methods
- Cell Statistics
  - When overlaying multiple raster layers, cell-based statistical analysis is often performed at the raster cell level.
- Neighbourhood Statistics
  - Neighbourhood statistics take the cell to be calculated as the centre, extend a certain range around it, and perform function operations based on these extended neighbouring cells to obtain the value for that cell.
- Zonal Statistics
  - Zonal statistics perform numerical statistical analysis on one dataset based on the zones of another dataset, including computing value ranges, maximum, minimum, standard deviation, etc. Zonal statistics operate on each zone, so the output result assigns the same single output value to each zone.

ISO Cluster
- ISO Cluster, i.e., Iterative Self-Organizing Clustering, is the most commonly used unsupervised classification algorithm. It first sets initial cluster centres and number of clusters, defines a similarity criterion function, adjusts all samples, then recomputes sample means as new cluster centres. During each iteration, all pixels are assigned to existing cluster centres based on the minimum Euclidean distance, aggregating pixels to the nearest mean in multi-dimensional attribute space, and new means are recalculated for each cluster centre. Through multiple merging and splitting processes, the pixel clustering analysis is finally completed, yielding a reasonably clustered result.

Basic principle of Maximum Likelihood Classification
- It assumes that the spectral characteristics of ground objects in training samples, like most random phenomena in nature, approximately follow a normal distribution. Using training samples, feature parameters such as class means, variances, and covariances can be calculated, thus obtaining the prior probability density functions of the populations. On this basis, for any pixel, the probability of belonging to each class is computed, and the class with the maximum probability is assigned as the classification result.

# 3D Analysis

How to create surface models?
- The most common method for constructing 3D surfaces is to sample points at different locations within the region and interpolate the sample points to generate a raster surface, thus approximating the real surface.

Forms and methods for creating 3D surfaces
- Using the ArcGIS 3D Analyst module, new 3D surfaces can be created from existing datasets. Two forms can be used to create 3D surfaces suitable for specific data analyses:
  - Regular grid (raster model)
  - Triangulated Irregular Network (TIN model)
- Two main methods for creating 3D surface models:
  - Interpolation
  - Triangulation

TIN (Triangulated Irregular Network)
- TINs are typically created from multiple vector data sources, including points, lines, and polygon features as input. The input features can contain different attributes, which are retained in the output TIN features, such as the relative accuracy of different data sources or attributes used to identify features (e.g., roads and lakes).

3D Surface Analysis
- What are the main components of ArcGIS 3D surface analysis?
  - Calculating 3D surface geometric parameters
  - Interactive 3D surface analysis
  - Visibility analysis
- Intervisibility Analysis
  - Intervisibility analysis determines whether the surface along a line of sight from an observer's position is visible or obstructed. It can be used to judge whether one point is visible from another.

Converting 2D features to 3D
- How to convert 2D features to 3D feature data?
  - Deriving elevation attribute values for features from a surface
    - Since surface data contain 3D attributes, surfaces can be used to create 3D features.
  - Using a feature attribute value as elevation
    - Field survey data often have elevation attributes; these can be used to convert to 3D features.
  - Converting from 3D layer to 3D feature class
    - 2D vector data can be displayed in 3D in ArcScene through extrusion; this 3D visualisation effect can be converted into true 3D geometry data.

# Spatial Statistical Analysis

Differences and Connections between Spatial Statistics and Classical Statistics
- Both are based on large-scale sampling, analysing frequency distributions, means, variances, and other relationships and their corresponding rules of sample attribute values to determine spatial distribution patterns and correlations.
- Spatial statistics of data considers not only sample values but also sample spatial locations and distances between samples.

Classification of Spatial Interpolation Methods
- Spatial interpolation can be classified from different perspectives, and different interpolation models require different prerequisites.
  - By interpolation region
    - Global interpolation
      - Global polynomial interpolation
    - Local interpolation
      - Inverse distance weighting
      - Radial basis functions
      - Local polynomial
      - Kriging
  - Some interpolation methods
    - Deterministic interpolation methods
      - Based solely on data models
        - Inverse distance weighting
        - Spline interpolation
        - Radial basis functions
        - Global (local) polynomial interpolation
      - Although deterministic interpolation predicts surface values based on similarity or smoothness among sample points, some deterministic interpolation models also account for spatial autocorrelation.
        - Inverse distance weighting
        - Modified inverse distance weighting models can remove certain trends.
    - Geostatistical interpolation methods
      - Also consider spatial autocorrelation of spatial phenomena.
        - Kriging and its variants

Exploratory Spatial Data Analysis (ESDA)
- Content and significance of ESDA
  - ESDA is a data analysis approach that, compared to traditional data analysis, places more emphasis on data integrity processing and cleaning before spatial modeling, graphical analysis of data distributions, descriptive characterisation of variables, comparing differences and relationships among data, and determining or transforming spatial distributions of data, with the aim of conducting subsequent spatial modeling based on a comprehensive understanding of the basic spatial characteristics of the data.
  - Since spatial statistical analysis is similar to classical statistics, many analysis models require data to meet specific distribution assumptions; thus, ESDA is particularly important for spatial statistical analysis.
- Histogram
  - A histogram classifies sample data according to a certain classification scheme (equal interval, standard deviation, etc.), counts the number of sample points falling into each class or the percentage of the total sample, and displays them as bar charts or histograms. Histograms can intuitively reflect the distribution characteristics and overall patterns of sample data, and can be used to test data distributions and identify outliers.
- Voronoi Diagram
  - A Voronoi diagram consists of a series of polygons formed around sample points. The Voronoi polygon for a sample point is generated such that any location within the polygon is closer to that sample point than to any other sample point. After Voronoi polygons are generated, adjacent points are defined as those sharing a common edge.

Spatial Interpolation and Geostatistical Simulation
- Deterministic Spatial Interpolation
  - Inverse Distance Weighting (IDW)
    - IDW is based on the principle that things that are closer are more similar; i.e., the closer two objects are, the more similar their properties, and vice versa. It performs weighted averaging with distances between interpolation points and sample points as weights: the closer a sample point is to the interpolation point, the larger its weight.
  - Global Polynomial Interpolation
    - Global polynomial interpolation uses a single polynomial calculated from the entire study area's sample dataset to predict values, fitting a plane or surface to represent the overall trend.
  - Local Polynomial Interpolation
    - While global polynomial interpolation uses one polynomial to fit the entire surface, local polynomial interpolation uses multiple polynomials, each within a specific overlapping neighbourhood. The neighbourhood can be defined using a search neighbourhood dialog.
- Geostatistical Point Interpolation
  - Kriging
    - Kriging is an interpolation method based on spatial autocorrelation that uses original data and the structure of the semivariogram to provide unbiased estimates of unknown sample points of regionalised variables. It is a core component of geostatistics.
  - Main workflow of Kriging interpolation
    ![image-1](/images/gis-knowledge/mubu-02.jpg)
  - Classification and applicable conditions of Kriging methods
    - Several types:
      - Ordinary Kriging
        - When the expected value of the attribute is unknown
      - Simple Kriging
        - When the expected value of the attribute is a known constant
      - Universal Kriging
        - When there is a dominant trend in the data
      - Co-Kriging
        - When two attributes of the same phenomenon are correlated and one is difficult to measure, co-kriging uses the other attribute to interpolate the former.
      - Log-normal Kriging
        - When data do not follow a normal distribution but do follow a log-normal distribution
      - Indicator Kriging
        - When only need to know whether attribute values exceed a certain threshold
      - Probability Kriging
      - Disjunctive Kriging
        - When data do not follow a bivariate normal distribution
  - Ordinary Kriging Interpolation
    - Ordinary kriging is a linear estimation of regionalised variables. It assumes that data variations follow a normal distribution and that the expected value of the regionalised variable Z is an unknown constant. The interpolation process is similar to weighted moving averages, but the weights are determined from spatial data analysis.

# Spatial Analysis Modeling

Spatial Analysis Modeling
- Spatial analysis modeling is a method that decomposes and abstracts specific spatial problems into spatial analysis models, uses spatial analysis as a tool, and combines GIS to study and simulate real-world spatial objects, thereby facilitating problem solving and planning.
- Four common types of models:
  - Suitability models
    - Agricultural applications, optimal site selection, road selection, etc.
  - Hydrological models
    - Water flow direction
  - Surface models
    - Analysing pollution levels at different locations in a region
  - Distance models
    - Optimal path selection from origin to destination, shortest path for postmen, etc.
- Model building workflow
  ![image-1](/images/gis-knowledge/mubu-03.jpg)

Diagrammatic Modeling
- Diagrammatic modeling uses intuitive graphical language to express a specific process model.

Model Formation Process
![image-1](/images/gis-knowledge/mubu-04.jpg)