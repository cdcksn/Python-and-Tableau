# LEGO
A Personal Project on LEGO 

In this project, we explore the LEGO sets that exisit, when they were created, and the most popular themes behind these sets. 

Acquire the Data:
1. We got this data from Kaggle: https://www.kaggle.com/datasets/rtatman/lego-database

2. We are using the following csvs: sets.csv and themes.csv

Clean the Data:
1. First import your libraries and import the csv files. 

![image](https://user-images.githubusercontent.com/68393151/207804490-7c25eb5d-d703-487a-a669-a5a2fe8ad98b.png)

2. Next, lets take a look at our data. 

![image](https://user-images.githubusercontent.com/68393151/207804648-07c5e78d-688e-46bc-823b-5e30780e3a8b.png)

3. Let's further explore our datasets by looking at the data types. 

![image](https://user-images.githubusercontent.com/68393151/207804891-82417374-99df-4627-83cc-0b260ae3037f.png)

4. Next up, let's look at the distribution of our data. 

![image](https://user-images.githubusercontent.com/68393151/207805101-9e501585-b5ea-4c41-a31f-123f0e757c71.png)

5. We noticed a null value earlier in the themes dataset. Let's count the nulls. 

![image](https://user-images.githubusercontent.com/68393151/207805356-49ebaea6-a488-4250-8575-7075ec3208f1.png)

It looks like we have quite a few nulls in the themes data set under the column parent_id. Perhaps those sets are orphans, since they don't have parents. We could exclude those rows, but we are not planning on using the parent_id column, so we'll hold off for now.

![image](https://user-images.githubusercontent.com/68393151/207806405-1b0bddf9-30d2-4a8a-9f25-46c4a80b4aad.png)

6. Let's check for duplicate rows. 

![image](https://user-images.githubusercontent.com/68393151/207806639-11bcc5f5-7069-4530-b466-564ac245c012.png)

7. Next, let's examine the distribution of the year column. Do we have any outliers? 

![image](https://user-images.githubusercontent.com/68393151/207806864-c089791d-1d11-4a0d-aed7-9e9ce37c2ae3.png)

Looks like our data is definetly skewed right, towards more recent years. There might be an outlier or two, but that data is significant in this instance, as it represents the first LEGO sets ever made. 

Visualize the Data:
1. Import CSVs into Tableau Public, link the data sources, create a dashboard with visualizations

![image](https://user-images.githubusercontent.com/68393151/207949810-a376ecaa-0339-45b9-9c4c-08fb7bd55187.png)

https://public.tableau.com/views/LEGOKaggleAnalysis/LEGOKaggleAnalysis?:language=en-US&:display_count=n&:origin=viz_share_link
