use fashion_review;
select * from reviews;
select count(*) as total_reviews
from review;

 select round(avg(rating), 2) as avg_rating from reviews;
 use fashion_review;
 select * from reviews
 limit 10;
 select `Department Name`, 
	round(avg(Rating), 2) as avg_rating
	from reviews
    where `Department Name` is not null
    AND TRIM(`Department Name`) <> ''
    group by `Department Name`
    order by avg_rating desc;	
    
    select `Class Name`,
			count(*) as review_count
		from reviews 
        where `Class Name` is not null
        and TRIM(`Class Name`) <> ''
        group by `Class Name`
        order by review_count DESC;
        
select 
	round(
			sum(case when `recommended IND`= 1 then 1 else 0 end)
				*100 / count(*),2
                ) as recommended_percentage
	from reviews;
    
select 
	case 
		when Age between 18 and 25 then '18-25'
        when Age between 26 and 35 then '26-35'
		when Age between 36 and 45 then '36-45'
        when Age between 46 and 55 then '46-55'
        when Age>=56 then '56+'
	END AS Age_group,
    count(*) as review_count,
    `Class Name`
from reviews
where `Class Name` is not null
and TRIM(`Class Name`) <> ''
group by Age_group, `Class Name`
order by Age_group, review_count;
select  
	Rating, count(*) as review_count,
    sum(
		case when `Recommended IND`=1 then 1 else 0 end) as recommendation,
	round(sum(
				case when `Recommended IND`=1 then 1 else 0 end)*100/ count(*), 2)
				as recommendation_percentage
		from reviews
        where Rating is not null
	group by Rating
    order by Rating;
use fashion_review;


select 
	Rating, `Class Name`,  `Review Text` 
from reviews
where
	Rating <= 2 and
	`Review Text` is not null and
    trim(`Review Text`) <> '';
	
select 
	count(*) as size_complaints
from reviews 
where Rating<=2
and `Review Text` is not null
and lower(`Review Text`) like '%size%';

select 
	count(*) as quality_complaints
from reviews
where Rating<=2 and 
	`Review Text` is not null
and lower(`Review Text`) like '%quality%';

select 
	count(*) as fabric_complaints
from reviews
where Rating<=2 and 
	`Review Text` is not null
and lower(`Review Text`) like '%fabric%';           

select 
	count(*) as comfort_complaints
from reviews
where Rating<=2 and 
	`Review Text` is not null
and lower(`Review Text`) like '%comfort%';     
				
select 
	count(*) as color_complaints
from reviews
where Rating<=2 and 
	`Review Text` is not null
and lower(`Review Text`) like '%color%';

select 
	count(*) as complaints
from reviews
where Rating<=2 ;

select 
`Class Name`, count(*) 
from reviews 
where Rating<=2 and `Class Name` is not null
group by `Class Name`;

select 
	`Class Name` , count(*) as total_reviews,
    sum(case when `Rating`<=2 then 1 else 0 end ) as low_rating_reviews,
    round(sum(case when `Rating`<=2 then 1 else 0 end) *100/count(*), 2) as poor_satisfaction_percentage
from reviews
where `Class Name` is not null and
	trim(`Class Name`)<> '' 
group by `Class Name`
order by poor_satisfaction_percentage desc;

select * from reviews limit 20;

select Rating,
	count(*) as total_review,
    round(avg(`Positive Feedback Count`),2) as avg_positive_rating
from reviews
where Rating is not null
group by Rating
order by total_review desc;

use fashion_review;
