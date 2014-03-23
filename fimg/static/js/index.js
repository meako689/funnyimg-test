var fimgApp = angular.module('fimgApp', []);

fimgApp.controller('imgController', ['$scope', '$http', function($scope, $http) {
    $http.get('/photostream/').success(function(data) {
        $scope.photos = data;
    });
}]);
