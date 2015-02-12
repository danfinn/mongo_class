use test;
db.places.find({
    location:{
        $near:  {
	    $geometry:  {
		type: "Point",
		coordinates: [-155.9760885,19.6174497]},  // current location at house in Kailua
		$maxDistance:20000000000000000
	}
    }
})
