package ksql.test.test.udafs;

import io.confluent.ksql.function.udf.Udf;
import io.confluent.ksql.function.udf.UdfDescription;
import io.confluent.ksql.function.udf.UdfParameter;

@UdfDescription(name = "movieAbbr", description = "creates movie abrreviation from name")
public class MovieAbbreviation {
	
	  @Udf(description = "Takes a string and creates string abbreviation")
	  public String movieAbbr(
	    @UdfParameter(value = "movieAbbr", description = "movie name") final String movieName) {
	    
		// split the movie name
	    String[] allWords = movieName.split(" ");
	    
	    // build a new string with first characters
	    StringBuilder finalAbbr = new StringBuilder();
	    for (String word: allWords) {
	    	finalAbbr.append(word.charAt(0));
	    }
	    
	    // return the new string in Upper case
		return finalAbbr.toString().toUpperCase();
	  }
}
