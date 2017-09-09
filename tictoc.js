function read(ascending=false,startAt= 	,endAt=-1){
  //root and questions refs
  var root = firebase.database().ref();
  var response = root.child('response');
  var employers = response.child('employers');
  //instantiates question list to be returned
  var employerList = [];
  //orders the questions in time order descending and then then listens for values
  employers.once('value',function(snapshot) {
    //iterates through each value in the snap
    snapshot.forEach(function(snap)
    {
      //grabs the text, tags, created by, key
      
      var name = snap.child('name').val();
      var industry = snap.child('industry').val();
      var overallRating = snap.child('overallRating').val();
      var cultureRating = snap.child('cultureAndValuesRating').val();
      var careerOpRating = snap.child('careerOpportunitiesRating').val();
      var compensationRating = snap.child('compensationAndBenefitsRating').val();
      var workLifeBalanceRating = snap.child('workLifeBalanceRating').val();
      var numRatings = snap.child('numberOfRatings').val();
      var pros= snap.child('featuredReview').child('pros').val();
      var cons = snap.child('featuredReview').child('cons').val();
      var employer = [name,industry,overallRating,cultureRating,careerOpRating,compensationRating,workLifeBalanceRating,numRatings,pros,cons];
      employerList.push(employer);
    });
    return employerListpl
  });