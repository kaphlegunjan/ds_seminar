package com.ksql.udf.demo;


import io.confluent.ksql.function.udaf.Udaf;
import io.confluent.ksql.function.udaf.UdafDescription;
import io.confluent.ksql.function.udaf.UdafFactory;


@UdafDescription(name = "minrating", description = "calculates average")
public class MinRating {
	
	@UdafFactory(description = "computes average of doubles")
	public static Udaf<Integer, Integer> createUdaf() {

	    return new Udaf<Integer, Integer>() {
	    	
		@Override
		public Integer aggregate(Integer value, Integer aggregate) {
			return (value < aggregate) ? value : aggregate;
		}

		@Override
		public Integer initialize() {
			return 0;
		}

		@Override
		public Integer merge(Integer aggregate1, Integer aggregate2) {
			return (aggregate1 < aggregate2) ? aggregate1 : aggregate2;
		}
			
	    };
	}
}
