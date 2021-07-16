angular.module('app', [])
.controller('MainController', function($scope) {
  $scope.numChildren = 10;
  $scope.items = [];
  for (var i = 100; i > 0; i--) {
    $scope.items.push(i);
  }
  $scope.items = $scope.items.reverse();

  $scope.containerStyle = {};
  $scope.childStyle = [];
  $scope.selected = 0;
  
  $scope.flexDirectionOptions = ['row', 'row-reverse', 'column', 'column-reverse'];
  $scope.containerStyle['flex-direction'] = $scope.flexDirectionOptions[0];
  
  $scope.flexWrapOptions = ['nowrap', 'wrap', 'wrap-reverse'];
  $scope.containerStyle['flex-wrap'] = $scope.flexWrapOptions[0];
  
  $scope.justifyContentOptions = ['flex-start', 'flex-end', 'center', 'space-between', 'space-around'];
  $scope.containerStyle['justify-content'] = $scope.justifyContentOptions[0];
  
  $scope.alignItemsOptions = ['flex-start', 'flex-end', 'center', 'baseline', 'stretch'];
  $scope.containerStyle['align-items'] = $scope.alignItemsOptions[0];
  
  $scope.containerStyle['align-content'] = $scope.alignItemsOptions[0];
  
  $scope.select = function(index) { $scope.selected = index; }
})
;