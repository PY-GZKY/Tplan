import request from '@/utils/request'

export function get_redis_data(query) {
  return request({
    url: '/monitor/redis',
    method: 'get',
    params: query
  })
}


export function get_mongo_data(query) {
  return request({
    url: '/monitor/mongo',
    method: 'get',
    params: query
  })
}
