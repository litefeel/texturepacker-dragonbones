// the filter function
var NegativeFilter = function(n)
{
	n = -n;
	return String(n);
};

// the filter name
NegativeFilter.filterName = "negative";

// register the filter
Library.addFilter("NegativeFilter");
