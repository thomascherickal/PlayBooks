import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
  Tooltip,
} from "@mui/material";
import PaginatedTable from "../PaginatedTable.js";
import { Link, useNavigate } from "react-router-dom";
import NoExistingPlaybook from "./NoExistingWorkflow.jsx";
import { Delete, Edit, History } from "@mui/icons-material";
import WorkflowActionOverlay from "./WorkflowActionOverlay.jsx";
import { useState } from "react";
import useToggle from "../../hooks/useToggle.js";

const WorkflowTableRender = ({ data, refreshTable }) => {
  const navigate = useNavigate();
  const { isOpen: isActionOpen, toggle } = useToggle();
  const [selectedWorkflow, setSelectedWorkflow] = useState({});

  const handleDeleteWorkflow = (item) => {
    setSelectedWorkflow(item);
    toggle();
  };

  const handleEditWorkflow = (id) => {
    navigate(`/workflows/${id}`);
  };

  const handleExecutionHistory = (id) => {
    navigate(`/workflows/executions/${id}`);
  };

  return (
    <>
      <Table stickyHeader>
        <TableHead>
          <TableRow>
            <TableCell className="!font-bold">Name</TableCell>
            <TableCell className="!font-bold">Playbooks</TableCell>
            <TableCell className="!font-bold">Schedule</TableCell>
            <TableCell className="!font-bold !text-center">
              Last Execution Time
            </TableCell>
            <TableCell className="!font-bold !text-center">
              Last Execution Status
            </TableCell>
            <TableCell className="!font-bold">Created by</TableCell>
            <TableCell className="!font-bold">Actions</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data?.map((item, index) => (
            <TableRow
              key={index}
              sx={{
                "&:last-child td, &:last-child th": { border: 0 },
              }}>
              <TableCell component="th" scope="row">
                <Link
                  to={`/workflows/${item.id}`}
                  className="text-violet-500 underline">
                  {item.name}
                </Link>
              </TableCell>
              <TableCell component="td" scope="row" className="!text-center">
                {item.playbooks?.length > 0
                  ? item.playbooks.map((e) => (
                      <div
                        className="p-1 text-xs border rounded bg-gray-50 cursor-pointer w-fit transition-all hover:bg-violet-500 hover:text-white"
                        key={e.id}>
                        <Link to={`/playbooks/${e.id}`}>{e.name}</Link>
                      </div>
                    ))
                  : "--"}
              </TableCell>
              <TableCell component="td" scope="row">
                <div className="flex flex-col text-xs gap-1">
                  <span className="text-sm font-bold">
                    {item.schedule?.type}
                  </span>
                  {item.schedule?.periodic?.cron_rule && (
                    <span className="border bg-gray-50 w-fit p-1 font-bold">
                      {item.schedule?.periodic?.cron_rule?.rule}
                    </span>
                  )}
                  {item.schedule?.periodic?.duration_in_seconds && (
                    <span className="border bg-gray-50 w-fit p-1">
                      For {item.schedule?.periodic?.duration_in_seconds} seconds
                    </span>
                  )}
                </div>
              </TableCell>
              <TableCell component="td" scope="row" className="!text-center">
                --
              </TableCell>
              <TableCell component="td" scope="row" className="!text-center">
                --
              </TableCell>
              <TableCell component="td" scope="row">
                {item.created_by}
              </TableCell>
              <TableCell component="td" scope="row">
                <div className="flex gap-2">
                  <button
                    className="rounded border border-violet-500 text-violet-500 hover:text-white hover:bg-violet-500 transition-all p-1"
                    onClick={() => handleEditWorkflow(item.id)}>
                    <Tooltip title="Edit this Workflow">
                      <Edit />
                    </Tooltip>
                  </button>
                  <button
                    className="rounded border border-violet-500 text-violet-500 hover:text-white hover:bg-violet-500 transition-all p-1"
                    onClick={() => handleDeleteWorkflow(item)}>
                    <Tooltip title="Remove this Workflow">
                      <Delete />
                    </Tooltip>
                  </button>
                  <button
                    className="rounded border border-violet-500 text-violet-500 hover:text-white hover:bg-violet-500 transition-all p-1"
                    onClick={() => handleExecutionHistory(item.id)}>
                    <Tooltip title="View execution history">
                      <History />
                    </Tooltip>
                  </button>
                </div>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      {!data?.length ? <NoExistingPlaybook /> : null}
      <WorkflowActionOverlay
        workflow={selectedWorkflow}
        isOpen={isActionOpen}
        toggleOverlay={toggle}
        refreshTable={refreshTable}
      />
    </>
  );
};

const WorkflowTable = ({
  workflowsList,
  total,
  pageSize,
  pageUpdateCb,
  tableContainerStyles,
  refreshTable,
}) => {
  return (
    <PaginatedTable
      renderTable={WorkflowTableRender}
      data={workflowsList ?? []}
      total={total}
      pageSize={pageSize}
      pageUpdateCb={pageUpdateCb}
      tableContainerStyles={tableContainerStyles ? tableContainerStyles : {}}
      refreshTable={refreshTable}
    />
  );
};

export default WorkflowTable;
