/**
* Facilities
* @namespace afya360.facilities.services
*/
(function () {
  'use strict';

  angular
    .module('afya360.facilities.services')
    .factory('Facilities', Facilities);

  Facilities.$inject = ['$http', 'djResource'];

  /**
  * @namespace Facilities
  * @returns {Factory}
  */
  function Facilities($http, djResource) {
    var Facilities = {
      all: all,
    };

    return Facilities;

    ////////////////////

    /**
    * @name all
    * @desc Get all Facilities
    * @returns {Promise}
    * @memberOf afya360.facilities.services.Facilities
    */
    function all() {
      var x = djResource('/api/v1/provinces/?format=json');
      // console.log(x.query());
      return x.query({limit:2});
      // return $http.get('/api/v1/provinces/?format=json');
    }
  }
})();