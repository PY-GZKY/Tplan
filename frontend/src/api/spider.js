import request from '@/utils/request'

export function get_project_list(query) {
  return request({
    url: '/projects',
    method: 'get',
    params: query
  })
}

// 创建项目
export const create_project = data => {
  return request({
      url: `/project/create`,
      method: 'POST',
      data: data
  })
};


// 删除项目 
export const delete_project = data => {
  return request({
      url: `/project/delete`,
      method: 'DELETE',
      data: data
  })
};


export function get_task_list(query) {
  return request({
    url: '/tasks',
    method: 'get',
    params: query
  })
}

// 创建任务
export const create_task = data => {
  return request({
      url: '/task/create',
      method: 'POST',
      data: data
  })
}

// 删除任务
export const delete_task = data => {
  return request({
      url: `/task/delete`,
      method: 'DELETE',
      data: data
  })
};

// 项目下的任务列表
export const task_list = query => {
  return request({
      url: `/project`,
      method: 'GET',
      params: query
  })
};

// 任务详情
export const task_detail = query => {
  return request({
      url: `/task/detail`,
      method: 'GET',
      params: query
  })
};

// 部署任务
export const deploy_task = data => {
  return request({
      url: `/task/deploy`,
      method: 'POST',
      data: data
  })
};



// 开启任务
export const start_task = data => {
  return request({
      url: `/task/run`,
      method: 'POST',
      data: data
  })
};

