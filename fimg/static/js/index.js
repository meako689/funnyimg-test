var fimgApp = angular.module('fimgApp', []);

fimgApp.controller('imgController', function($scope, $http, $timeout) {
    $scope.photos = [];
    $scope.filteredPhotos = [];
    $scope.loadingMore = false;
    $scope.filterText = '';

    $scope.loadMore = function(){
      $scope.loadingMore = true;
      var params = {
        offset : $scope.filteredPhotos.length,
        limit : 20,
        tag: $scope.filterText
      }

      $http.get('/photostream/',{'params':params}).success(function(data) {
          $scope.photos=$scope.photos.concat(data);
          $scope.loadingMore = false;
      });
    }

    var tempFilterText = '',
        filterTextTimeout;
    $scope.$watch('searchText', function(val){
      if (filterTextTimeout) $timeout.cancel(filterTextTimeout);
      tempFilterText = val;
      filterTextTimeout = $timeout(function() {
          $scope.filterText = tempFilterText;
          $scope.loadMore();
      }, 450); // delay 

    });
});

fimgApp.directive("scroll", function ($window) {
    //endless scrolling
    return function(scope, element, attrs) {
        angular.element($window).bind("scroll", function() {
          if (this.scrollY+this.innerHeight >= this.document.body.scrollHeight-100) {
            if (!scope.loadingMore) scope.loadMore();
          }
        });
    };
});
