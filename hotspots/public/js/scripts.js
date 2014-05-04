var baseURL = 'http://{s}.tile.cloudmade.com/{API}/{map_style}/256/{z}/{x}/{y}.png';

var base = L.tileLayer(baseURL, { 
	API: '9315dcdc627b4feab430d377cd7cb978', 
	map_style: '1714' 
	});

var denverLatLon = [39.7392, -104.9847];

$.getJSON('/zones').done(function( data ) {
		 var zoneMixed = L.geoJson(data, {
                   style: {color: "#ff0000"},
	  	   filter: function(feature, layer) {
				return feature.properties.zone_general == 'Mixed Use';
                            }
                    });
		 var zoneCommercial = L.geoJson(data, {
                   style: {color: "#0000ff"},
	  	   filter: function(feature, layer) {
				return feature.properties.zone_general == 'Commercial';
                            }
                    });
		 var zoneIndustrial = L.geoJson(data, {
                   style: {color: "#191970"},
	  	   filter: function(feature, layer) {
				return feature.properties.zone_general == 'Industrial';
                            }
                    });
		 var zoneSpecial = L.geoJson(data, {
                   style: {color: "#ffD700"},
	  	   filter: function(feature, layer) {
				return feature.properties.zone_general == 'Special';
                            }
                    });

                    /**
                     * Add zone checkbox handling
                     */
                    $('#mixedZones').change(function(e){
                        if ($(this).is(':checked')) {
                            map.addLayer(zoneMixed);
                        } else {
                            map.removeLayer(zoneMixed);
                        }
                    });
                    $('#commercialZones').change(function(e){
                        if ($(this).is(':checked')) {
                            map.addLayer(zoneCommercial);
                        } else {
                            map.removeLayer(zoneCommercial);
                        }
                    });
                    $('#industrialZones').change(function(e){
                        if ($(this).is(':checked')) {
                            map.addLayer(zoneIndustrial);
                        } else {
                            map.removeLayer(zoneIndustrial);
                        }
                    });
                    $('#specialZones').change(function(e){
                        if ($(this).is(':checked')) {
                            map.addLayer(zoneSpecial);
                        } else {
                            map.removeLayer(zoneSpecial);
                        }
                    });
                    $('#restaurants').change(function(e){
                        if ($(this).is(':checked')) {
                            map.addLayer(zoneJson);
                        } else {
                            map.removeLayer(zoneJson);
                        }
                    });
			})
			.fail(function( jqxhr, textStatus, error ) {
				var err = textStatus + ", " + error;
				console.log( "Request Failed: " + err );
			});




var map = L.map('map', {layers: [base]}).setView(denverLatLon, 12);

L.control.scale().addTo(map);


//custom size for this example, and autoresize because map style has a percentage width
var heatmap = new L.TileLayer.WebGLHeatMap({size: 2000, alphaRange: 0.1, opacity: 0.6}); 



function generateDataSet(scale, valueRange, numberOfPoints) {
	var data = [];

	for (var i = 0; i < numberOfPoints; ++i) {
		var latVariance = (Math.random()-0.5)*scale;
		var Lat = denverLatLon[0] + latVariance;
		var Lon = denverLatLon[1] + (Math.random()-0.5)*scale;
		var value = valueRange*Math.random();
		//var value = valueRange*latVariance*1000;
		data.push([Lat, Lon, value]);
	}
	return data;
}
/*
var dataSets = [generateDataSet(0.1, 50, 500), 
				generateDataSet(0.1, 100, 250),
				generateDataSet(0.1, 200, 50)];
*/
var dataSets = [];


var initialSliderValue = 0.5;
var sliderVals = [];
var numberOfSliders = 3;

for (var i = 0; i < numberOfSliders; i++) {
	sliderVals[i] = initialSliderValue;
}

heatmap.clearData();

function updateHeatMap(multipliers) {
	if (!multipliers) {
		multipliers = [];
		for (var i = 0, len = dataSets.length; i < len; i++) {
			multipliers[i] = sliderVals[i];
		}
	}

	heatmap.setData([]);
	for (var i=0, numberOfDataSets = dataSets.length; i<numberOfDataSets; i++) {
		if (dataSets[i] !== undefined && dataSets[i].length !== undefined) {
			for (var j = 0, setLength = dataSets[i].length; j < setLength; j++) {
				heatmap.addDataPoint(dataSets[i][j][0], dataSets[i][j][1], 
				dataSets[i][j][2] * multipliers[i] );
			}
		}
	}
	heatmap.update();
}


$( document ).ready(function () {
	'use strict';

	// Sidebar controls
	$("#menu-toggle").click(function(e) {
		e.preventDefault();
		$("#wrapper").toggleClass("active");
	});

	var sliderOptions = {
		min: 0,
		max: 1,
		step: 0.01,
		value: initialSliderValue,
		formater: function(val) {
			return val.toFixed(2);
		}
	};
	$('.slider').slider(sliderOptions);

	//$('.slider').on('slideStop', function (e) {
	$('.slider').on('slide', function (e) {
		if ($(this).hasClass('heatmap')) {
			switch( $(this).attr('id') ) {
				case 'slider2':
					sliderVals[0] = e.value;
					break;
				case 'slider3':
					sliderVals[1] = e.value;
					break;
				case 'slider4':
					sliderVals[2] = e.value;
					break;
			}
			
			var multipliers = [];
			for (var i = 0, len = dataSets.length; i < len; i++) {
				multipliers[i] = sliderVals[i];
			}

			updateHeatMap(multipliers);
		}
	});

	/* 
	*  alternatively, if you have intensities set for each point, 
	*  as in above, you can skip the for loop and add the whole dataset 
	*  with heatmap.setData(dataPoints) 
	*/

	map.addLayer(heatmap);


	function formatData( data, selectValueFunction) {
		var formattedData = [], point, lat, lon, value;
		for (var i = 0, len = data.length; i < len; i++ ) {
			if (data[i].geometry){
			  lat = data[i].geometry.coordinates[1];
			  lon = data[i].geometry.coordinates[0];
			} else if (data[i].properties.latitude){
                          lat = data[i].properties.latitude;
                          lon = data[i].properties.longitude;
                        } else {
		          continue;	
			}

			value = selectValueFunction(data[i].properties);
			formattedData.push([lat, lon, value]);
		}
		return formattedData;
	}

	var requests = [];

	function loadData(route, dataIndex, options, formatDataFunction) {
		var request = $.getJSON( route, options)
			.done(function( data ) {
				//broadband = data;
				var formattedData = formatData(data.features, formatDataFunction);
				dataSets[dataIndex] = formattedData;
				console.log('request loaded');
			})
			.fail(function( jqxhr, textStatus, error ) {
				var err = textStatus + ", " + error;
				console.log( "Request Failed: " + err );
			});

		requests.push(request);
	}

	//'/broadband_speeds?attrs=actualdown&bbox=-105.0847,39.6392,-104.8847,39.8392'
	var broadbandRequestOptions = { };
	loadData('/broadband_speeds?attrs=actualdown', 0, broadbandRequestOptions, function (properties) {
		return properties.actualdown; 
	});

	var cellularsRequestOptions = { };
	loadData('/cellulars?attrs=devicesignalstrength,latitude,longitude', 1, cellularsRequestOptions, function (properties) {
		return properties.devicesignalstrength * -1; 
	}); 

// '/parking_meters?bbox=-105.0847,39.6392,-104.8847,39.8392&attrs=null'
	var parkingMeterRequestOptions = { };
	loadData('/parking_meters?attrs=Null', 2, parkingMeterRequestOptions, function (properties) {
		return 1; 
	}); 

	//bbox=xmin,ymin,xmax,ymax
	//$( '/broadband_speeds?attrs=actualdown&bbox=-105.0847,39.6392,-104.8847,39.8392')
	/*
	var broadbandRequest = $.getJSON( 'data/broadband-subset.json')
		.done(function( data ) {
			//broadband = data;
			var broadband = formatData(data.features, function (properties) {
				return properties.actualdown; 
			});
			dataSets[1] = broadband;
		})
		.fail(function( jqxhr, textStatus, error ) {
			var err = textStatus + ", " + error;
			console.log( "Request Failed: " + err );
		});
*/
/*
	//$.getJSON( '/parking_meters?bbox=-105.0847,39.6392,-104.8847,39.8392&attrs=null')
	$.getJSON( '/data/parking_meters-subset.json' )
		.done(function( data ) {
			var parkingMeters = formatData(data.features, function (properties) {
				return 1; 
			});
			dataSets[2] = parkingMeters;
		})
		.fail(function( jqxhr, textStatus, error ) {
			var err = textStatus + ", " + error;
			console.log( "Request Failed: " + err );
		});
	$.getJSON( '/cellulars')
		.done(function( data ) {
			var cellular = data;
		})
		.fail(function( jqxhr, textStatus, error ) {
			var err = textStatus + ", " + error;
			console.log( "Request Failed: " + err );
		});

*/
	$.when.apply(this, requests).done(function () {
		console.log('finished loading');
		updateHeatMap();
	});
});
