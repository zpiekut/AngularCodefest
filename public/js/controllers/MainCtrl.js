angular.module('MainCtrl', [])
	
  .controller('MainController', ['$scope', '$http',
  	function($scope, $http) {
      $scope.tagline = 'To the moon and back!';	
      getEvents();
       function getEvents() {
	    $http.get('/api/events')
	      .success(function(data) {
	        $scope.events = data;
	      });
	  }

	  function initCal() {
        $(function () {
          // wait till load event fires so all resources are available
          $scope.$calendar = $('#calendar').fullCalendar({
            defaultDate: '2015-02-12',
			editable: true,
		  	eventLimit: true, // allow "more" link when too many events
			events: $scope.events
          });
        });
      };
    }
]);