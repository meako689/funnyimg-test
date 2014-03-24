var fimgApp = angular.module('fimgApp', []);

fimgApp.controller('imgController', function($scope, $http) {
    $scope.photos = [];
    $scope.filteredPhotos = [];
    $scope.loadingMore = false;

    $scope.loadMore = function(){
      $scope.loadingMore = true;
      var params = {
        offset : $scope.filteredPhotos.length,
        limit : 20,
        tag: $scope.filterItems
      }

      $http.get('/photostream/',{'params':params}).success(function(data) {
          $scope.photos=$scope.photos.concat(data);
          $scope.loadingMore = false;
      });
    }
    $scope.loadMore();
    $scope.$watch('filterItems', function(filterItems){
      if (!$scope.loadingMore && filterItems.length>2){
          $scope.loadMore();
          console.log('moar');
      }
    });
});

fimgApp.directive("scroll", function ($window) {
    return function(scope, element, attrs) {
        angular.element($window).bind("scroll", function() {
          if (this.scrollY+this.innerHeight >= this.document.body.scrollHeight-100 && !scope.loadingMore) {
            scope.loadingMore = true;
            scope.loadMore();
          }
        });
    };
});
