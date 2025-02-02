import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableRow,
} from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";

import { renderTimestamp } from "../../utils/DateUtils";
import PaginatedTable from "../PaginatedTable";
import { useState } from "react";
import Tooltip from "@mui/material/Tooltip";

import { Link, useNavigate } from "react-router-dom";
import NoExistingPlaybook from "./NoExistingPlaybook";
import styles from "./playbooks.module.css";
import useToggle from "../../hooks/useToggle";
import PlaybookActionOverlay from "./PlaybookActionOverlay";
import { ContentCopy } from "@mui/icons-material";
import { useDispatch } from "react-redux";
import { copyPlaybook } from "../../store/features/playbook/playbookSlice.ts";
import { useLazyGetPlaybookQuery } from "../../store/features/playbook/api/index.ts";
import Loading from "../common/Loading/index.tsx";
import { COPY_LOADING_DELAY } from "../../constants/index.ts";

const PlaybookTableRender = ({ data, refreshTable, showDelete = true }) => {
  const navigate = useNavigate();
  const { isOpen: isActionOpen, toggle } = useToggle();
  const [selectedPlaybook, setSelectedPlaybook] = useState({});
  const [triggerGetPlaybook] = useLazyGetPlaybookQuery();
  const dispatch = useDispatch();
  const [copyLoading, setCopyLoading] = useState(false);

  const handleDeletePlaybook = (playbook) => {
    setSelectedPlaybook(playbook);
    toggle();
  };

  const handleCopyPlaybook = async (id) => {
    setCopyLoading(true);
    const res = await triggerGetPlaybook({ playbookId: id }).unwrap();
    dispatch(copyPlaybook(res));
    setTimeout(() => {
      navigate("/playbooks/create");
    }, COPY_LOADING_DELAY);
  };

  // const handleExecutionHistory = (id) => {
  //   navigate(`/playbooks/executions/${id}`);
  // };

  if (copyLoading) {
    return <Loading title="Copying your playbook..." />;
  }

  return (
    <>
      <Table stickyHeader>
        <TableHead>
          <TableRow>
            <TableCell className={styles["tableTitle"]}>Name</TableCell>
            <TableCell className={styles["tableTitle"]}>Created At</TableCell>
            <TableCell className={styles["tableTitle"]}>Created By</TableCell>
            {showDelete && (
              <TableCell className={styles["tableTitle"]}>Actions</TableCell>
            )}
          </TableRow>
        </TableHead>
        <TableBody>
          {data?.map((item, index) => (
            <TableRow
              key={index}
              sx={{
                "&:last-child td, &:last-child th": { border: 0 },
              }}>
              <TableCell component="td" scope="row">
                <Link to={`/playbooks/${item.id}`} className={styles["link"]}>
                  {item.name}
                </Link>
              </TableCell>
              <TableCell component="td" scope="row">
                {renderTimestamp(item.created_at)}
              </TableCell>
              <TableCell component="td" scope="row">
                {item.created_by}
              </TableCell>
              {showDelete && (
                <TableCell component="td" scope="row">
                  <div className="flex gap-2">
                    <button
                      className={styles["pb-button"]}
                      onClick={() => handleCopyPlaybook(item.id)}>
                      <Tooltip title="Copy this Playbook">
                        <ContentCopy />
                      </Tooltip>
                    </button>
                    <button
                      className={styles["pb-button"]}
                      onClick={() => handleDeletePlaybook(item)}>
                      <Tooltip title="Remove this Playbook">
                        <DeleteIcon />
                      </Tooltip>
                    </button>
                    {/* <button
                      className="rounded border border-violet-500 text-violet-500 hover:text-white hover:bg-violet-500 transition-all p-1"
                      onClick={() => handleExecutionHistory(item.id)}>
                      <Tooltip title="View execution history">
                        <History />
                      </Tooltip>
                    </button> */}
                  </div>
                </TableCell>
              )}
            </TableRow>
          ))}
        </TableBody>
      </Table>
      {!data?.length ? <NoExistingPlaybook /> : null}
      <PlaybookActionOverlay
        playbook={selectedPlaybook}
        isOpen={isActionOpen}
        toggleOverlay={toggle}
        refreshTable={refreshTable}
      />
    </>
  );
};

const PlaybookTable = ({
  playbookList,
  total,
  pageSize,
  pageUpdateCb,
  tableContainerStyles,
  refreshTable,
  showDelete,
}) => {
  return (
    <PaginatedTable
      renderTable={PlaybookTableRender}
      data={playbookList ?? []}
      showDelete={showDelete}
      total={total}
      pageSize={pageSize}
      pageUpdateCb={pageUpdateCb}
      tableContainerStyles={tableContainerStyles ? tableContainerStyles : {}}
      refreshTable={refreshTable}
    />
  );
};

export default PlaybookTable;
