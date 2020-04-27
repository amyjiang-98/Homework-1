for $x in //book 
order by xs:float($x/price) 
return $x/title

