---
title: "一批公开地理空间数据集的整理笔记"
description: "横跨地形、土地覆被、地表温度、夜间灯光、建筑高度和人口的公开数据集速查：谁做的、什么分辨率、覆盖哪些年份、怎么引用、哪里有坑。"
date: 2026-10-07
tags: ["地理数据", "数据整理"]
comments: true
ShowToc: true
TocOpen: false
---
围绕城市地表状态的这几类数据——从 30 米地形到 1 公里夜间灯光，从 1984 年的城市扩张到 2025 年的土地覆被——各自是从哪来的、什么分辨率、该引用谁，平时很难一次说清。

这篇文章就是一份整理笔记。**需要说明的是：本文各数据集的参数一律以官方文档和原始论文为准**。个别整理过程中实测的数值只用于与公开资料交叉核对，不作为权威指标。

## 一、全局速查

| 数据集 | 类型 | 空间分辨率 | 时间范围 | 来源机构 |
|---|---|---|---|---|
| TRIMS LST | 全天候地表温度 | 1 km | 2000–2024 | 国家青藏高原科学数据中心 |
| MODIS LST | 地表温度 | 1 km | 2000 年至今 | NASA（Terra / Aqua） |
| ECOSTRESS L2 LSTE | 地表温度与发射率 | 70 m | 2018 年至今 | NASA / JPL |
| CLCD | 土地覆被（一级类） | 30 m | 1985–2025 | 武汉大学 |
| GLC_FCS30D | 土地覆被（精细分类） | 30 m | 1985–2022 | 中科院空天信息创新研究院 |
| PANDA | 人造夜间灯光 | 1 km | 1984–2020 | 清华 / 深圳国家超算中心等 |
| CNBH10m | 建筑高度 | 10 m | — | Wu 等（RSE 2023） |
| Landsat C2 L2 | 多光谱 + 地表温度 | 30 m（热红外 100 m） | 1982 年至今 | USGS / NASA |
| ASTER GDEM v3 | 数字高程 | 1 弧秒（约 30 m） | 2000–2013 观测 | NASA / METI |
| SRTM | 数字高程 | 1 弧秒（约 30 m） | 2000 年 2 月 | NASA / NGA |
| WorldPop | 人口栅格 | 100 m / 1 km | 2015–2030 | 南安普顿大学 |
| OpenStreetMap | 道路/水系/铁路等矢量 | 矢量 | 持续更新 | OSM 社区（Geofabrik 分发） |

## 二、地表温度

### TRIMS LST —— 把「有云就缺」这件事解决掉

热红外遥感的死穴是云：光学卫星看到云，地表温度就是空的。TRIMS LST 用「再分析数据 + 热红外遥感」的融合方法把缺测补上，做成空间无缝的**全天候**地表温度。

- **全称**：中国陆域及周边逐日 1 km 全天候地表温度数据集（TRIMS LST；2000–2024）
- **方法**：增强型再分析与热红外遥感融合（E-RTM），原始方法见 Zhang et al. (2021, *RSE*)
- **分辨率与频率**：1 km，逐日 4 次（Terra 白天/夜间、Aqua 白天/夜间）
- **范围**：72°E–135°E，19°N–55°N，含港澳台，暂不含南海诸岛
- **投影**：Albers 等积投影
- **数值**：整型存储，**像元值 ÷ 100 = 开尔文**；缺失值统一为 0（约占总量 0.1%–0.5%）
- **命名**：`TRIMS_Terra/Aqua + 年份 + 年积日 + D/N`，例如 `TRIMS_Aqua2024001D.tif`
- **精度**：以 MODIS LST 为参考，白天/夜间平均偏差（MBE）为 0.09 K / −0.03 K，偏差标准差 1.45 K / 1.17 K；基于 19 个站点的实测检验，MBE 为 −2.26 K 至 1.73 K，RMSE 为 0.80 K 至 3.68 K，且晴空与非晴空条件下无显著差异
- **额外福利**：同时提供 MODIS 过境时间文件（View_Time），把观测时刻也一并给你。原始值 0–240、背景值 255，乘官方 Scale_Factor 后是地方太阳时（有效 0–24，背景 25.5），生产时统一转成了 UTC
- **DOI**：`10.11888/Meteoro.tpdc.271252`

一个小坑：随附的英文 Readme 有些版本写的是 **2000–2022**，而数据集页面的元数据已更新到 **2000–2024**。买数据前先确认你拿到的是哪一版。

### MODIS LST —— 上面那份数据的地基

TRIMS 的主要输入就是它，所以先看这一份。

- **产品**：MOD11A1（Terra）与 MYD11A1（Aqua），MODIS 第 6.1 版（v061）
- **分辨率与频率**：**1 km，逐日**。Terra 约在地方时 10:30 过境（白天）/ 22:30（夜间），Aqua 约 13:30 / 01:30
- **数据集**：`LST_Day_1km` 与 `LST_Night_1km`，另配 `QC_Day` / `QC_Night` 质量控制层
- **数值**：整型存储，**Scale Factor = 0.02，单位开尔文**——像元值 × 0.02 才是 K。这是整个领域最经典的坑之一，漏乘 0.02 会得到几万开尔文的「温度」
- **网格**：**正弦投影（Sinusoidal）**，不是等经纬度网格，与其它数据叠加前必须重投影
- **许可**：开放（NASA LP DAAC）

MODIS LST 的长处是**时间连续、全球一致、从 2000 年至今**；短处同样清楚——**1 km 在城市尺度上太粗**，而且**有云即缺**。这恰恰是 TRIMS 存在的理由：借用 MODIS LST 的空间相关性加上再分析数据的低频信息，把云底下的空洞补回来。

### ECOSTRESS —— 国际空间站上的「应急热成像」

ECOSTRESS 挂在国际空间站上，轨道不是太阳同步，所以它**不按固定时刻过境**——这既是缺点也是特点：它能捕捉到日内温度变化，还能对火山、干旱、灌溉等事件做应急响应。

- **产品**：L2 LSTE（地表温度与发射率），由温度发射率分离（TES）方法反演
- **分辨率**：70 m × 70 m（由原始 38 m × 68 m 重采样）
- **精度**：与全球验证站点总体 RMSE ≈ 1.07 K，r² > 0.988，MAE ≈ 0.4 K；另有验证工作报告不确定度小于 1 K
- **波段构成**：除 LST 外还给 5 个发射率波段（Emis1–Emis5，uint8，Scale Factor 0.002，有效范围 0.49–1.0）以及质量控制层，官方算法说明见 LP DAAC 的 ECOSTRESS Level-2 用户指南
- **层级**：L1B GEO（地理定位）、L2 LSTE（原始 swath）、L2G LSTE（投影到 70 m 网格）、L2T LSTE（分幅切片，如 `51RTP`）
- **版本**：v001（`ECOSTRESS_L2_LSTE_...`）与 v002（`ECOv002_L2_LSTE_...`）并存，建议统一用 v002
- **获取**：NASA LP DAAC

注意 L2T 是**分幅**产品，文件名里的 `51RTP` 是 MGRS 图幅号；而 L2G 是已经放到规则 70 m 网格上的，做时间序列分析优先用 L2G。

## 三、土地覆被与地表覆盖

### CLCD —— 中国的年度土地覆被

- **全称**：China Land Cover Dataset（中国年度土地覆盖数据集）
- **分辨率**：30 m；**时间范围**：**1985 年起逐年**。官方记录（国家冰川冻土沙漠科学数据中心，2023 年发布）覆盖 1985–2022；Zenodo 上的最新版本已标到 2025 年（v1.0.5）
- **分类**：9 个一级类——耕地、林地、灌木、草地、水体、冰雪、裸地、不透水面、湿地；随数据附一份 `CLCD_classificationsystem.xlsx` 类别表
- **方法**：在 Google Earth Engine 上用了 335,709 景 Landsat 影像；训练样本来自 CLUD 稳定样本加人工目视解译；分类器是**随机森林**，之后用时空滤波 + 逻辑推理做后处理。2022 年之后因 USGS 不再维护 Collection 1，改用它家的 Collection 2 SR 继续更新
- **投影**：Albers 等积投影，proj4 字符串是
  `+proj=aea +lat_1=25 +lat_2=47 +lat_0=0 +lon_0=105 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs`
  （中央经线 105°E，双标准纬线 25°N / 47°N）。文件名里的 `_albert_` / `_albert_province.zip` 就是 Albers 的意思，不是人名
- **文件形式**：全国单文件 `CLCD_v01_YYYY_albert.tif`，以及按省打包的 `CLCD_v01_YYYY_albert_province.zip`；当前版本已导出为 **Cloud Optimized GeoTIFF**，内置金字塔与色表，加载更快
- **许可**：**CC BY 4.0**
- **引用**：Yang, J. & Huang, X. (2021). The 30 m annual land cover and its dynamics in China from 1990 to 2019. *Earth System Science Data*, 13, 3907–3925. DOI: `10.5194/essd-13-3907-2021`；数据 DOI `10.5281/zenodo.8176941`

CLCD 的定位是「**宏观趋势够用、精细分类不够用**」。它把城市建成区、农田、林地分得很干净，适合做长时序变化检测；但你要是想区分「常绿阔叶林」和「落叶针叶林」，它给不了。

### GLC_FCS30D —— 35 个二级类的精细分类

这个数据集名字里的 **D** 是 Dynamic（动态）的意思，是这批数据里分类体系最细的一份。

- **全称**：GLC_FCS30D（global 30 m land-cover dynamic monitoring product with fine classification system）
- **生产者**：刘良云、张肖，中国科学院空天信息创新研究院
- **别和 GLC_FCS30 搞混**：`GLC_FCS30` 是更早的版本，发布于若干离散年份；`GLC_FCS30D` 是它的**逐年动态**版本，分类体系更细、时间连续。两者文件名只差一个字母 `D`，选数据时务必看清
- **时间范围**：**1985–2022**。2000 年以前每 5 年一期，**2000 年以后逐年**
- **分类体系**：35 个二级类。核心编码如 `10` 雨养农田、`20` 灌溉农田、`51/52` 常绿阔叶林、`71/72` 常绿针叶林、`120` 灌木、`130` 草地、`190` **不透水面**、`210` **水体**、`220` 冰雪，`0` 与 `250` 为填充值
- **精度**：基本分类体系（10 个一级类）总体精度 **80.88% ± 0.27%**；LCCS level-1（17 类）为 73.24% ± 0.30%
- **文件组织**：每个图幅拆成两个文件——`GLC_FCS30D_19851995_5years_*`（3 波段，对应 1985/1990/1995）和 `GLC_FCS30D_20002022_*`（**23 波段**，对应 2000–2022 逐年）。**波段号即年份**，用切片时别把波段顺序搞反
- **引用**：Zhang, X., Liu, L., Chen, X., Gao, Y., Xie, S., Mi, J. (2021). GLC_FCS30: global land-cover product with fine classification system at 30 m using time-series Landsat imagery. *ESSD*, 13, 2753–2776. DOI: `10.5194/essd-13-2753-2021`。另有 GWL_FCS30（湿地，2023）与 GISD30（不透水面，2022）两篇配套论文
- **数据使用政策（重要）**：官方文档明确写道——如果你打算在科学分析论文中使用该数据，**强烈建议提前联系作者征求意见，并在致谢中体现其贡献或考虑共同署名**。这不是普通的 CC 许可，别默认可以随便用

### PANDA —— 把夜间灯光倒推到 1984 年

- **全称**：中国长时间序列逐年人造夜间灯光数据集（1984–2020）；英文缩写 PANDA（Prolonged Artificial Nighttime-light Dataset）
- **发布方**：国家超级计算深圳中心、清华大学、可持续发展大数据国际研究中心、香港大学；作者包括张立贤、任浙豪、徐冰、付昊桓、陈斌、宫鹏
- **分辨率与范围**：1 km，逐年，覆盖中国，1984–2020 共 37 期
- **意义**：DMSP-OLS 夜间灯光从 1992 年才有，VIIRS 从 2012 年才有，中间还有两者不可比的问题。PANDA 首次把夜光观测**延拓到 1984 年**，并统一了长时序口径，因此特别适合做城市化、经济活动时空变化研究
- **论文**：*Scientific Data*, 2024. DOI: `10.1038/s41597-024-03223-1`（该论文入选 ESI 高被引）
- **数值特征**：整型存储，大片区域为 0（无灯光），亮度越高像元越少——这是判断它是不是夜光产品的一个直观特征

### CNBH10m —— 把「楼有多高」也算出来

建筑高度一直是城市研究里最难拿的变量之一：它没法从二维影像直接读出来，也不像地表覆盖那样有成熟的全球产品。CNBH-10m 是**中国第一份 10 米分辨率的建筑高度估计**，思路是把多源对地观测数据与机器学习结合起来。

- **全称**：CNBH-10m（A first Chinese building height estimate at 10 m resolution）
- **论文**：Wu, W. 等，*A first Chinese building height estimate at 10 m resolution (CNBH-10 m) using multi-source earth observations and machine learning*，**Remote Sensing of Environment**，2023
- **数据沉积**：Zenodo（记录号 `7064268`、`7923866`）
- **实测特征**：10 m 分辨率，单波段浮点，单位应为米；按 **3°×3°** 分幅，瓦片编号形如 `CNBH10m_X121Y29`（X 为经度、Y 为纬度），另有 EPSG:4326 版本；投影为 UTM（如 51N / EPSG:32651）
- **有效像元极稀疏**（抽样约 3%）——这符合预期：建筑高度只在建成区有意义，大片非建成区是无效值

两点提醒：一是**取用前务必先确认 NoData 是怎么标的**，这种稀疏数据很容易被当成 0 混进统计；二是**具体的 RMSE / MAE 请以论文原文为准**，别引用二手数字。

## 四、卫星影像

### Landsat Collection 2 Level-2（L2SP）

这是这批数据里最「标准」的一份，也是最值得长期依赖的一份。

- **产品含义**：Collection 2 Level-2 科学产品（L2SP）同时给出**地表反射率（SR）**与**地表温度（ST）**，已经做过大气校正，可以直接用，不必自己从 DN 值开始反演
- **分辨率**：多光谱 30 m；热红外原始 100 m，产品中重采样到 30 m（做热红外分析时心里要有数，真正的空间分辨率是 100 m）
- **Tier 分级**：`T1` 为 Tier 1（几何与辐射质量最好，适合时序分析）；`T2` 为 Tier 2（质量次之，适合单期使用）
- **传感器**：Landsat 5 TM（`LT05`）、Landsat 7 ETM+（`LE07`）、Landsat 8 OLI/TIRS（`LC08`）、Landsat 9（`LC09`）
- **命名**：`LXSS_L2SP_PATHROW_YYYYMMDD_PROCESSINGDATE_COLLECTION_TIER_*`，例如 `LC08_L2SP_119039_20200908_20200919_02_T1_...` 表示 Landsat 8、Path 119 / Row 039、2020-09-08 成像
- **常用波段**：`QA_PIXEL`（云掩膜，做时序一定要用）、`QA_RADSAT`（饱和像元）、`*_ST_B10`（地表温度）
- **已知问题**：**Landsat 7 自 2003 年 5 月起扫描行校正器（SLC）故障**，影像上出现规律性条带（SLC-off），2003 年之后用 LE07 数据必须做条带处理或直接避开
- **许可**：美国联邦政府作品，**公有领域**，可自由使用

## 五、地形

### ASTER GDEM（ASTGTM）

- **全称**：ASTER Global Digital Elevation Model，由 NASA 与日本 METI 联合生产
- **分辨率**：1 弧秒，约 30 m；按 1°×1° 分幅，编号形如 `ASTGTM_N30E119`
- **覆盖**：83°N–83°S，全球
- **版本**：v3 是目前推荐版本
- **许可**：免费开放

### SRTM

- **全称**：Shuttle Radar Topography Mission，2000 年 2 月由航天飞机用 11 天完成观测，NASA 与 NGA 生产
- **分辨率**：1 弧秒（约 30 m，SRTMGL1）与 3 弧秒（约 90 m，SRTMGL3）；目前对公众开放的是 1 弧秒全球版
- **格式**：`.hgt` 是无头文件的裸格式——大端序、16 位有符号整数，**空洞值为 −32768**，一格一个高程值，用之前必须自己补投影信息
- **许可**：公有领域

**哪个更好用？** 两者都是 30 米级，但误差特性不同：SRTM 在有植被和陡峭地形处容易产生偏差（雷达波打到树冠而非地面），ASTER GDEM 在平坦区和云覆盖区噪声更大。做地形分析时建议**两个都拿来做交叉验证**，而不是只信一个。

## 六、人口

### WorldPop

WorldPop 最容易踩的坑不在分辨率，而在**版本口径**——同一个国家会同时存在好几套产品，差别很大。

- **全称**：WorldPop，南安普顿大学主导的开放人口栅格项目，2013 年由 AfriPop / AsiaPop / AmeriPop 三个项目合并而来
- **命名解析**：以 `chn_pop_2024_CN_100m_R2025A_v1.tif` 为例——`chn` 中国、`pop` 人口数、`2024` 年份、`CN` 国家、`100m` 分辨率、`R2025A` **发布版本**、`v1` 版本号
- **`R2025A` 是新口径**：它属于 **WorldPop Global 2（Global_2015_2030）** 项目，覆盖 **2015–2030 逐年**，其中 2021 年及以后是基于联合国《世界人口展望》2024 版的推算值——而不是老版 Global_2000_2020 的 2000–2020。**要跨年或跨国比较，先确认手头文件属于哪个项目**
- **`pop` 不等于 `pd`**：文件名里 `_pop_` 是**人口数（count）**，`_pd_` 是**人口密度（people / km²）**，两者千万别混用
- **数值与缺失值**：Global 2 为 Float32、EPSG:4326，1 km 版本对应 30 弧秒（0.008333°）；**缺失值是 −99999**
- **方法**：基于随机森林的 dasymetric 重分配；国家总量对齐 UN WPP 2024；先掩掉水体等不可居住区域，再用夜间灯光、坡度、高程、气候等协变量建模
- **许可**：CC BY 4.0
- **引用**：Bondarenko M. 等，*The spatial distribution of population in 2015–2030 at a resolution of 30 arc (approximately 1 km at the equator) R2025A version v1*，WorldPop，南安普顿大学，DOI `10.5258/SOTON/WP00845`（该 DOI 对应 1 km 版本，100 m 版本请按产品页单独确认）；并按惯例注明 www.worldpop.org

## 七、矢量基础数据

### OpenStreetMap（经 Geofabrik 分发的 Shapefile 包）

- **数据来源**：OSM 社区；Geofabrik 提供按国家/省级别的免费 shapefile 分发包，文件名形如 `zhejiang-latest-free.shp.zip`
- **图层**：`gis_osm_roads_free_1`（道路）、`gis_osm_water_free_1`（水系）、`gis_osm_railways_free_1`（铁路）、`gis_osm_adminareas_a_free_1`（行政区）等
- **许可（重点）**：**ODbL 1.0**。署名是必须的，而且如果你基于它生成了「衍生数据库」并对外发布，还需要**以相同方式共享**。只在论文里画个图通常只需署名，但若把裁剪后的路网打包发布，就要留意同一许可的要求
- **已知问题**：覆盖度城乡差异大、属性不规范、道路分级体系与国内标准不一致，不适合直接当权威数据用

### 行政边界与十段线

- **常见来源**：阿里云 DataV.GeoAtlas、GADM、Natural Earth 等；常见的 `中国_省.geojson`、`中国_县.geojson` 等文件即属这一类
- **合规提醒（重要）**：在中国境内公开发布地图，必须保证**领土完整**——包括南海诸岛、藏南、台湾等，并正确表示**十段线**（原九段线，2014 年后地图上通常表示十段）。这是硬性要求，不是可选项
- **正确做法**：使用**自然资源部标准地图服务系统**（`bzdt.ch.mnr.gov.cn`）提供的标准地图作为底图，或严格按其规范绘制；直接拿第三方 GeoJSON 出图而不做审查，是很容易出问题的
- 审图号制度适用于公开出版的地图；学术论文插图也建议使用标准底图，降低风险

## 八、使用这些数据：版本对照与常见坑

先看几对最容易混的版本——「同名不同物」的情况相当多：

| 容易混淆 | 区别 | 怎么选 |
|---|---|---|
| `GLC_FCS30` / `GLC_FCS30D` | 前者是若干离散年份；后者 1985–2022 **逐年**、分类更细 | 做变化检测用 D；只做单期制图两者都行 |
| WorldPop `Global_2000_2020` / `Global_2015_2030` | 时间范围不同，对齐的联合国基准版本也不同（`R2025A` 属后者） | 跨年比较前先固定到同一个项目 |
| WorldPop `_pop_` / `_pd_` | 人口数（count）/ 人口密度（people·km⁻²） | 要总量用 `pop`，要强度用 `pd` |
| `CLCD_v01` / 后续版本 | v01 主要基于 Landsat Collection 1；2022 年之后改用 Collection 2 SR | 长时序尽量固定在同一个版本，避免口径跳变 |
| Landsat `T1` / `T2` | Tier 1 几何与辐射质量最好；Tier 2 次之 | 时序分析用 T1，T2 只用来补 T1 的空缺 |
| ECOSTRESS `L2` / `L2G` / `L2T` | 原始 swath / 已重采样到 70 m 网格 / 分幅切片 | 时序分析用 L2G；按图幅下载用 L2T |
| ASTER GDEM / SRTM | 光学立体测量 vs 雷达干涉测量，误差特性相反 | 两个都取，互为交叉验证 |
| 「开尔文」的几种写法 | MODIS ×0.02；TRIMS ÷100；ECOSTRESS 另有 scale | 逐产品查 scale factor，别凭记忆 |

然后才是最常见的坑：

1. **投影不统一**。上述数据里同时存在 Albers 等积投影（TRIMS、CLCD）、UTM（CNBH、部分 DEM）、WGS84 经纬度（PANDA、WorldPop、GLC_FCS30D）。做叠加分析前必须先统一投影，而且**面积统计一定要用等积投影**。
2. **数值不是原值**。TRIMS 的 DN 要 ÷100 得开尔文，MODIS 的 DN 要乘 scale factor，View_Time 要乘 0.1 再理解成 UTC 小时。不看 scale factor 直接用，结果会离谱。
3. **缺失值五花八门**。TRIMS 用 0，SRTM 用 −32768，PANDA 用 −32768，DEM 用 32767，CLCD 用 0，WorldPop Global 2 用 −99999。**同一份分析里混用多套数据时，先统一缺失值标记**，否则 0 会被当成「合法的零温度」参与统计。
4. **时间口径不一致**。CLCD 是自然年，Landsat 是成像时刻，TRIMS 是逐日 4 次瞬时，PANDA 是年度合成。跨数据做时间序列时，「同一年」其实并不严格可比。
5. **波段即年份**。GLC_FCS30D 的 23 波段文件，波段号对应年份，别按「波段从 1 开始」随便取。
6. **热红外的真实分辨率**。Landsat 热红外是 100 m 重采样到 30 m，看着是 30 m 网格，实际有效信息量是 100 m 级。

**如果真要把它们拼起来用，建议的处理顺序是：**

1. **先定投影。** 选一个等积投影（上述数据中 CLCD 与 TRIMS 都用 Albers、中央经线 105°E），把所有栅格重投影过去；**面积统计一律在这个投影下做**，经纬度网格上算面积等于自找麻烦。
2. **再对齐网格。** 挑一个基准栅格（通常选分辨率最细、覆盖最全的那个），离散型数据（土地覆被、DEM、整数化的夜光）用**最近邻**重采样，连续型数据（LST、人口）才用双线性。**别对分类数据用三次卷积**——它会插值出根本不存在的类别码。
3. **统一缺失值。** 把各家的 NoData（0 / −32768 / 32767 / −99999）先归一到同一个标记（NaN 或一个明确的哨兵值），再进入任何统计。
4. **换算物理量。** 把所有 DN 乘上各自的 scale factor，落成开尔文 / 米 / 人这样的真实单位。
5. **最后才谈特征工程与建模。** 到这一步再做归一化、波段组合、时间合成。

顺序错了会很痛苦：**先归一化再统一缺失值**，会把 NoData 当成有效极值参与缩放；**先建模再重投影**，等于把重采样误差直接写进特征。

## 九、引用与许可速查

| 数据集 | 是否可自由使用 | 需要做什么 |
|---|---|---|
| TRIMS LST | 需署名 | 注明数据来源与作者；DOI `10.11888/Meteoro.tpdc.271252` |
| ECOSTRESS | 开放 | 引用产品与 LP DAAC |
| CLCD | 开放 | 引用 Yang & Huang (2021) |
| GLC_FCS30D | **有附加要求** | 官方建议**提前联系作者**并在致谢体现或考虑共同署名 |
| PANDA | 开放 | 引用 *Scientific Data* 论文与数据中心 |
| Landsat C2 L2 | **公有领域** | 无强制要求，仍建议致谢 USGS/NASA |
| ASTER GDEM / SRTM | 开放 / 公有领域 | 建议致谢 NASA、METI、NGA |
| WorldPop | CC BY 4.0 | 署名 |
| OpenStreetMap | **ODbL 1.0** | 署名；发布衍生数据库需相同方式共享 |
| 行政边界 / 标准地图 | 视来源而定 | 公开发布前核对**审图号与标准地图**要求 |

## 十、取用数据时的两点实务提醒

**1. 大文件下载后先做完整性检查。** WorldPop Global 2 的全国 100 m 文件有数百 MB，下载中断或存储损坏并不罕见。典型症状是 GDAL / rasterio 直接报错，例如 `TIFFReadDirectory: Failed to read directory at offset ...`；此时读文件头会发现 TIFF 版本号字段异常（正常应为 42），且第一个 IFD 声称的条目数远超实际。遇到这种情况直接重新下载，不要试图修补。

**2. TRIMS 要确认 Terra 与 Aqua 都拿到了。** 产品提供逐日 4 次观测（Terra 白天/夜间 + Aqua 白天/夜间）。校验方法：DAY / NIGHT 目录下的数据文件与 View_Time 过境时间文件应各有 365 天 × 2 个平台。缺哪个平台就补哪个——只拿到 Aqua 意味着日内分析实际只有 2 个观测时刻，而不是产品宣称的 4 个。

---

## 十一、参考来源

本文涉及的官方入口（按文中出现顺序）。部分站点（LP DAAC、Zenodo）可能出现跳转或短时故障，链接若失效请按 DOI 检索。

- **TRIMS LST**：[国家青藏高原科学数据中心](https://data.tpdc.ac.cn/)，DOI `10.11888/Meteoro.tpdc.271252`
- **MODIS LST**：[NASA LP DAAC MOD11A1 v061](https://lpdaac.usgs.gov/products/mod11a1v061/)
- **ECOSTRESS**：[LP DAAC ECO_L2G_LSTE v002](https://lpdaac.usgs.gov/products/eco_l2g_lstev002/)；算法说明见 [ECOSTRESS Level-2 用户指南](https://lpdaac.usgs.gov/documents/1574/ECOL2_User_Guide_V2.pdf)
- **CLCD**：[国家冰川冻土沙漠科学数据中心记录](https://www.ncdc.ac.cn/portal/metadata/9de270f3-b5ad-4e19-afc0-2531f3977f2f)（proj4、许可与方法说明出自这里）；数据 DOI `10.5281/zenodo.8176941`，论文 DOI `10.5194/essd-13-3907-2021`
- **GLC_FCS30D**：论文 [GLC_FCS30, ESSD 2021](https://doi.org/10.5194/essd-13-2753-2021)；数据由中国科学院空天信息创新研究院发布
- **PANDA**：[Scientific Data 论文](https://www.nature.com/articles/s41597-024-03223-1) · [数据页](https://data.tpdc.ac.cn/en/data/e755f1ba-9cd1-4e43-98ca-cd081b5a0b3e/)，DOI `10.1038/s41597-024-03223-1`
- **CNBH-10m**：[Zenodo 数据沉积](https://zenodo.org/records/7064268)；论文见 *Remote Sensing of Environment*（2023）
- **Landsat**：[USGS EarthExplorer](https://earthexplorer.usgs.gov/) · [Collection 2 说明](https://www.usgs.gov/landsat-missions/landsat-collection-2)
- **ASTER GDEM v3**：[LP DAAC ASTGTM v003](https://lpdaac.usgs.gov/products/astgtmv003/)
- **SRTM**：[LP DAAC SRTMGL3 v003](https://lpdaac.usgs.gov/products/srtmgl3v003/)
- **WorldPop**：[Global 2 / R2025A 发布说明（PDF）](https://data.worldpop.org/repo/prj/Global_2015_2030/R2025A/doc/Global2_Release_Statement_R2025A_v1.pdf)，DOI `10.5258/SOTON/WP00845`
- **OpenStreetMap**：[Geofabrik 下载](https://download.geofabrik.de/) · [版权与许可](https://www.openstreetmap.org/copyright)
- **标准地图**：[自然资源部标准地图服务系统](https://bzdt.ch.mnr.gov.cn/)

*说明：文中标注为实测的数值（文件大小、栅格元数据、完整性诊断等）仅用于与公开资料交叉核对，不代表数据集的官方指标；各数据集的权威参数请以官方文档与原始论文为准。文中链接与 DOI 建议在使用前再次核实版本。*
