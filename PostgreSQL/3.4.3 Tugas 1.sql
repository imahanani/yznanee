Select *
from fitnes_tracker ; --565 rows

Select count (distinct brand_name) as unique_brand
from fitnes_tracker; -- banyak brand? count (distint brand_name)| 19 brand 

Select min(selling_price) as harga_terendah_xiaomi
from fitnes_tracker
where brand_name = 'Xiaomi' ; -- harga jual terendah dari produk brand Xiaomi

Select avg(rating) as avg_rating_samsung
from fitnes_tracker
where brand_name = 'SAMSUNG' ; -- rata-rata rating produk Samsung | Select distinct brand_name from fitnes_tracker | kapital letter |

Select max(average_battery_life_days) as max_battery_life
from fitnes_tracker  ; -- nilai daya tahan baterai tertinggi dari seluruh produk

Select sum(reviews) as total_reviewers_fossil
from fitnes_tracker
where brand_name = 'FOSSIL'; -- banyak orang ulas brand Fossil
