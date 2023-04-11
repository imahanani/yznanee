Select *
from fitnes_tracker; --565 rows

Select brand_name , avg(original_price)
from fitnes_tracker
group by brand_name; -- rata-rat harga awal tiap brand |19 rows
--select count(distinct brand_name) from fitnes_tracker;
