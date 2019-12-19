package com.ksql.udf.demo;

import io.confluent.ksql.function.udaf.TableUdaf;
import io.confluent.ksql.function.udaf.UdafFactory;
import io.confluent.ksql.function.udf.UdfDescription;

@UdfDescription(name = "average", description = "calculates average")
public class Average {
	  @UdafFactory(description = "sums longs")
	  
	  // Can be used with table aggregations
	  public static TableUdaf<String, Double> average() {
	    return new TableUdaf<String, Double>() {

			public Double aggregate(String arg0, Double arg1) {
				// TODO Auto-generated method stub
				return null;
			}

			public Double initialize() {
				// TODO Auto-generated method stub
				return null;
			}

			public Double merge(Double arg0, Double arg1) {
				// TODO Auto-generated method stub
				return null;
			}

			public Double undo(String arg0, Double arg1) {
				// TODO Auto-generated method stub
				return null;
			}
	    };
	  }
}
