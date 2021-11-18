<template>
  <div class="app-container">
    <el-row :gutter="10" class="panel-group">
      <el-col :xs="12" :sm="12" :lg="8" class="card-panel-col">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-people">
            <svg-icon icon-class="guide" class-name="card-panel-icon" />
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">工人数</div>
            <count-to
              :start-val="0"
              :end-val="this.num.workers_num"
              :duration="2600"
              class="card-panel-num"
            />
          </div>
        </div>
      </el-col>
      <el-col :xs="12" :sm="12" :lg="8" class="card-panel-col">
        <div class="card-panel" @click="handleTask()">
          <div class="card-panel-icon-wrapper icon-message">
            <svg-icon icon-class="bug" class-name="card-panel-icon" />
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">任务数</div>
            <count-to
              :start-val="0"
              :end-val="this.num.functions_num"
              :duration="3000"
              class="card-panel-num"
            />
          </div>
        </div>
      </el-col>
      <el-col :xs="12" :sm="12" :lg="8" class="card-panel-col">
        <div class="card-panel" @click="handleResult()">
          <div class="card-panel-icon-wrapper icon-money">
            <svg-icon icon-class="time" class-name="card-panel-icon" />
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">结果集</div>
            <count-to
              :start-val="0"
              :end-val="this.num.results_num"
              :duration="3200"
              class="card-panel-num"
            />
          </div>
        </div>
      </el-col>
    </el-row>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="taskList"
      border
      fit
      highlight-current-row
      style="width: 100%"
    >
      <el-table-column align="center" label="队列" min-width="310px">
        <template slot-scope="{ row }">
          <el-tag type="" size="mini">{{ row.queue_name }}</el-tag>
        </template>
      </el-table-column>

      <el-table-column min-width="310px" align="center" label="工人">
        <template slot-scope="{ row }">
  
            <el-tag type="success" size="mini">{{ row.worker_name }}</el-tag>
    
        </template>
      </el-table-column>

      <el-table-column min-width="80px" align="center" label="状态">
        <template slot-scope="{ row }">
          <el-tag v-if="row.is_action" type="success" size="mini">运行中</el-tag>
          <el-tag v-else type="info" size="mini">离线</el-tag>
        </template>
      </el-table-column>

      <el-table-column min-width="120px" align="center" label="队列任务">
        <template slot-scope="{ row }">
          <span>{{ row.queued }}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="120px" align="center" label="已完成">
        <template slot-scope="{ row }">
          <span>{{ row.j_complete }}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="150px" align="center" label="进行中">
        <template slot-scope="{ row }">
          <span>{{ row.j_ongoing }}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="150px" align="center" label="执行失败">
        <template slot-scope="{ row }">
          <span>{{ row.j_failed }}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="150px" align="center" label="重试次数">
        <template slot-scope="{ row }">
          <span>{{ row.j_retried }}</span>
        </template>
      </el-table-column>
    </el-table>

    <pagination
      v-show="total > 0"
      :total="total"
      :page.sync="listQuery.page"
      :limit.sync="listQuery.limit"
      @pagination="getWorkerList"
    />
  </div>
</template>

<script>
import CountTo from "vue-count-to";
import { get_all_workers, index } from "@/api/arq";
import waves from "@/directive/waves"; // waves directive
import Pagination from "@/components/Pagination"; // secondary package based on el-pagination

export default {
  inject: ["reload"],
  name: "workerList",
  components: { Pagination, CountTo },

  directives: { waves },
  data() {
    return {
      tableKey: 0,
      taskList: null,
      cronTaskList: null,
      projectList: null,
      total: 0,
      listLoading: false,
      listQuery: {
        page: 1,
        limit: 10,
      },
      num:{
        workers_num:null,
        functions_num:null,
        results_num:null

      }
    };
  },
  created() {
    this.getIndex();
    this.getWorkerList();
  },
  methods: {
    getIndex() {
      index({}).then((response) => {
        this.num.workers_num = response.results.workers_num;
        this.num.functions_num = response.results.functions_num;
        this.num.results_num = response.results.results_num;
        this.total = response.total || 2;
        setTimeout(() => {}, 1.5 * 1000);
      });
    },
    getWorkerList() {
      get_all_workers({}).then((response) => {
        this.taskList = response.result;
        this.total = response.total || 2;
        setTimeout(() => {}, 1.5 * 1000);
      });
    },

    handleTask() {
      const self = this;
      self.$router.push(`/arq/task`);
    },
    handleJob() {
      // const self = this;
      // self.$router.push(`/arq/job`);
    },
    handleWorker() {
      // const self = this;
      // self.$router.push(`/arq/worker`);
    },
    handleResult() {
      const self = this;
      self.$router.push(`/arq/job`);
    },
  },
};
</script>


<style lang="scss" scoped>
.panel-group {
  margin-top: 18px;

  .card-panel-col {
    margin-bottom: 32px;
  }

  .card-panel {
    height: 108px;
    cursor: pointer;
    font-size: 12px;
    position: relative;
    overflow: hidden;
    color: #666;
    background: #fff;
    box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.05);
    border-color: rgba(0, 0, 0, 0.05);

    &:hover {
      .card-panel-icon-wrapper {
        color: #fff;
      }

      .icon-people {
        background: #40c9c6;
      }

      .icon-message {
        background: #36a3f7;
      }

      .icon-money {
        background: #f4516c;
      }

      .icon-shopping {
        background: #34bfa3;
      }
    }

    .icon-people {
      color: #40c9c6;
    }

    .icon-message {
      color: #36a3f7;
    }

    .icon-money {
      color: #f4516c;
    }

    .icon-shopping {
      color: #34bfa3;
    }

    .card-panel-icon-wrapper {
      float: left;
      margin: 14px 0 0 14px;
      padding: 16px;
      transition: all 0.38s ease-out;
      border-radius: 6px;
    }

    .card-panel-icon {
      float: left;
      font-size: 48px;
    }

    .card-panel-description {
      float: right;
      font-weight: bold;
      margin: 26px;
      margin-left: 0px;

      .card-panel-text {
        line-height: 18px;
        color: rgba(0, 0, 0, 0.45);
        font-size: 16px;
        margin-bottom: 12px;
      }

      .card-panel-num {
        font-size: 20px;
      }
    }
  }
}

@media (max-width: 550px) {
  .card-panel-description {
    display: none;
  }

  .card-panel-icon-wrapper {
    float: none !important;
    width: 100%;
    height: 100%;
    margin: 0 !important;

    .svg-icon {
      display: block;
      margin: 14px auto !important;
      float: none !important;
    }
  }
}
</style>
