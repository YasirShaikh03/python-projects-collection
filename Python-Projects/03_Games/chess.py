import pygame
import chess
import sys

# ── Constants ──────────────────────────────────────────────────────────────────
WIDTH, HEIGHT = 720, 720
BOARD_SIZE = 640
SQUARE = BOARD_SIZE // 8
OFFSET_X = (WIDTH - BOARD_SIZE) // 2
OFFSET_Y = (HEIGHT - BOARD_SIZE) // 2

LIGHT = (240, 217, 181)
DARK  = (181, 136, 99)
HIGHLIGHT   = (246, 246, 130, 180)
LEGAL_DOT   = (0, 0, 0, 60)
LEGAL_CAPTURE = (246, 246, 130, 120)
CHECK_COLOR = (220, 50, 50, 160)
SELECTED_COLOR = (106, 168, 79, 200)
BG_COLOR    = (30, 30, 30)
STATUS_BG   = (22, 22, 22)
TEXT_COLOR  = (220, 220, 200)
ACCENT      = (200, 160, 80)

UNICODE_PIECES = {
    chess.PAWN:   {chess.WHITE: '♙', chess.BLACK: '♟'},
    chess.ROOK:   {chess.WHITE: '♖', chess.BLACK: '♜'},
    chess.KNIGHT: {chess.WHITE: '♘', chess.BLACK: '♞'},
    chess.BISHOP: {chess.WHITE: '♗', chess.BLACK: '♝'},
    chess.QUEEN:  {chess.WHITE: '♕', chess.BLACK: '♛'},
    chess.KING:   {chess.WHITE: '♔', chess.BLACK: '♚'},
}


# ── Helpers ────────────────────────────────────────────────────────────────────
def square_to_pixel(sq, flipped=False):
    """Return top-left pixel (x, y) for a chess square."""
    file = chess.square_file(sq)
    rank = chess.square_rank(sq)
    if flipped:
        file = 7 - file
        rank = 7 - rank
    x = OFFSET_X + file * SQUARE
    y = OFFSET_Y + (7 - rank) * SQUARE
    return x, y


def pixel_to_square(px, py, flipped=False):
    """Return chess.Square from pixel coords, or None if outside board."""
    bx = px - OFFSET_X
    by = py - OFFSET_Y
    if not (0 <= bx < BOARD_SIZE and 0 <= by < BOARD_SIZE):
        return None
    file = bx // SQUARE
    rank = 7 - (by // SQUARE)
    if flipped:
        file = 7 - file
        rank = 7 - rank
    return chess.square(file, rank)


def draw_board(surface, board, selected, legal_squares, flipped, last_move):
    for rank in range(8):
        for file in range(8):
            sq = chess.square(file, rank)
            x, y = square_to_pixel(sq, flipped)
            color = LIGHT if (file + rank) % 2 == 0 else DARK
            pygame.draw.rect(surface, color, (x, y, SQUARE, SQUARE))

            # Last-move highlight
            if last_move and sq in (last_move.from_square, last_move.to_square):
                s = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
                s.fill(HIGHLIGHT)
                surface.blit(s, (x, y))

            # Selected square
            if sq == selected:
                s = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
                s.fill(SELECTED_COLOR)
                surface.blit(s, (x, y))

            # King in check
            piece = board.piece_at(sq)
            if (piece and piece.piece_type == chess.KING
                    and piece.color == board.turn and board.is_check()):
                s = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
                s.fill(CHECK_COLOR)
                surface.blit(s, (x, y))

    # Legal move indicators
    for lsq in legal_squares:
        lx, ly = square_to_pixel(lsq, flipped)
        if board.piece_at(lsq):  # capture
            s = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
            s.fill(LEGAL_CAPTURE)
            surface.blit(s, (lx, ly))
        else:  # empty dot
            s = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
            pygame.draw.circle(s, LEGAL_DOT, (SQUARE // 2, SQUARE // 2), SQUARE // 6)
            surface.blit(s, (lx, ly))


def draw_pieces(surface, board, piece_font, flipped):
    for sq in chess.SQUARES:
        piece = board.piece_at(sq)
        if piece:
            sym = UNICODE_PIECES[piece.piece_type][piece.color]
            x, y = square_to_pixel(sq, flipped)
            # Shadow
            shadow = piece_font.render(sym, True, (0, 0, 0))
            surface.blit(shadow, (x + SQUARE // 2 - shadow.get_width() // 2 + 2,
                                   y + SQUARE // 2 - shadow.get_height() // 2 + 2))
            # Piece
            color = (255, 255, 255) if piece.color == chess.WHITE else (30, 30, 30)
            img = piece_font.render(sym, True, color)
            surface.blit(img, (x + SQUARE // 2 - img.get_width() // 2,
                                y + SQUARE // 2 - img.get_height() // 2))


def draw_coordinates(surface, coord_font, flipped):
    files = 'abcdefgh'
    ranks = '12345678'
    for i in range(8):
        f = files[i] if not flipped else files[7 - i]
        r = ranks[7 - i] if not flipped else ranks[i]
        # File labels (bottom)
        txt = coord_font.render(f, True, DARK if i % 2 == 0 else LIGHT)
        surface.blit(txt, (OFFSET_X + i * SQUARE + SQUARE - 12,
                            OFFSET_Y + BOARD_SIZE - 14))
        # Rank labels (left)
        txt2 = coord_font.render(r, True, LIGHT if i % 2 == 0 else DARK)
        surface.blit(txt2, (OFFSET_X + 3, OFFSET_Y + i * SQUARE + 3))


def draw_status(surface, board, status_font, move_count):
    pygame.draw.rect(surface, STATUS_BG, (0, 0, WIDTH, OFFSET_Y))
    pygame.draw.rect(surface, STATUS_BG, (0, HEIGHT - OFFSET_Y, WIDTH, OFFSET_Y))

    # Title
    title = status_font.render("CHESS", True, ACCENT)
    surface.blit(title, (20, OFFSET_Y // 2 - title.get_height() // 2))

    # Turn / result
    if board.is_checkmate():
        winner = "Black" if board.turn == chess.WHITE else "White"
        msg = f"Checkmate! {winner} wins"
        col = (220, 80, 80)
    elif board.is_stalemate():
        msg = "Stalemate — draw"
        col = ACCENT
    elif board.is_insufficient_material():
        msg = "Draw — insufficient material"
        col = ACCENT
    elif board.is_check():
        turn = "White" if board.turn == chess.WHITE else "Black"
        msg = f"{turn} to move — CHECK!"
        col = (220, 80, 80)
    else:
        turn = "White" if board.turn == chess.WHITE else "Black"
        msg = f"{turn} to move"
        col = TEXT_COLOR

    txt = status_font.render(msg, True, col)
    surface.blit(txt, (WIDTH // 2 - txt.get_width() // 2,
                        OFFSET_Y // 2 - txt.get_height() // 2))

    # Move counter
    mc = status_font.render(f"Move {move_count}", True, (120, 120, 100))
    surface.blit(mc, (WIDTH - mc.get_width() - 20,
                       OFFSET_Y // 2 - mc.get_height() // 2))

    # Bottom bar hints
    hints = [
        ("R", "Reset"),
        ("F", "Flip"),
        ("U", "Undo"),
        ("ESC", "Quit"),
    ]
    small = pygame.font.SysFont("segoeui", 13)
    x = 20
    for key, label in hints:
        k = small.render(f"[{key}]", True, ACCENT)
        l = small.render(f" {label}", True, (120, 120, 100))
        y = HEIGHT - OFFSET_Y + (OFFSET_Y - k.get_height()) // 2
        surface.blit(k, (x, y))
        surface.blit(l, (x + k.get_width(), y))
        x += k.get_width() + l.get_width() + 20


def promotion_dialog(surface, color, dialog_font):
    """Simple promotion picker; returns chosen piece type."""
    options = [chess.QUEEN, chess.ROOK, chess.BISHOP, chess.KNIGHT]
    syms = [UNICODE_PIECES[p][color] for p in options]
    labels = ["Queen", "Rook", "Bishop", "Knight"]

    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    surface.blit(overlay, (0, 0))

    box_w, box_h = 360, 130
    bx = WIDTH // 2 - box_w // 2
    by = HEIGHT // 2 - box_h // 2
    pygame.draw.rect(surface, (45, 40, 35), (bx, by, box_w, box_h), border_radius=10)
    pygame.draw.rect(surface, ACCENT, (bx, by, box_w, box_h), 2, border_radius=10)

    title = dialog_font.render("Promote pawn to:", True, TEXT_COLOR)
    surface.blit(title, (bx + box_w // 2 - title.get_width() // 2, by + 10))

    rects = []
    for i, (sym, label) in enumerate(zip(syms, labels)):
        rx = bx + 20 + i * 82
        ry = by + 50
        r = pygame.Rect(rx, ry, 72, 64)
        rects.append((r, options[i]))
        pygame.draw.rect(surface, (60, 55, 50), r, border_radius=6)
        s = dialog_font.render(sym, True,
            (255, 255, 255) if color == chess.WHITE else (30, 30, 30))
        surface.blit(s, (rx + 36 - s.get_width() // 2, ry + 4))
        lbl = pygame.font.SysFont("segoeui", 11).render(label, True, (160, 150, 130))
        surface.blit(lbl, (rx + 36 - lbl.get_width() // 2, ry + 48))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect, piece_type in rects:
                    if rect.collidepoint(event.pos):
                        return piece_type
        pygame.time.wait(30)


# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess — Pygame + python-chess")
    clock = pygame.time.Clock()

    # Fonts — use system fonts that support chess Unicode
    piece_font  = pygame.font.SysFont("segoeuisymbol,symbola,freesans", 54)
    status_font = pygame.font.SysFont("segoeui,dejavusans", 18)
    coord_font  = pygame.font.SysFont("segoeui,dejavusans", 13, bold=True)
    dialog_font = pygame.font.SysFont("segoeuisymbol,symbola,freesans", 42)

    board      = chess.Board()
    selected   = None        # currently selected square
    legal_sqrs = []          # legal destination squares for selected piece
    flipped    = False
    last_move  = None
    move_count = 1

    running = True
    while running:
        screen.fill(BG_COLOR)

        draw_board(screen, board, selected, legal_sqrs, flipped, last_move)
        draw_coordinates(screen, coord_font, flipped)
        draw_pieces(screen, board, piece_font, flipped)
        draw_status(screen, board, status_font, move_count)

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    board = chess.Board()
                    selected = legal_sqrs = []; last_move = None; move_count = 1
                elif event.key == pygame.K_f:
                    flipped = not flipped
                elif event.key == pygame.K_u:
                    if board.move_stack:
                        board.pop()
                        last_move = board.peek() if board.move_stack else None
                        selected = None; legal_sqrs = []
                        move_count = max(1, move_count - 1)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if board.is_game_over():
                    continue
                sq = pixel_to_square(*event.pos, flipped)
                if sq is None:
                    selected = None; legal_sqrs = []; continue

                if selected is None:
                    piece = board.piece_at(sq)
                    if piece and piece.color == board.turn:
                        selected = sq
                        legal_sqrs = [m.to_square for m in board.legal_moves
                                      if m.from_square == sq]
                else:
                    # Try to make a move
                    promotion = None
                    piece = board.piece_at(selected)
                    if (piece and piece.piece_type == chess.PAWN):
                        rank = chess.square_rank(sq)
                        if (piece.color == chess.WHITE and rank == 7) or \
                           (piece.color == chess.BLACK and rank == 0):
                            promotion = promotion_dialog(screen, piece.color, dialog_font)

                    move = chess.Move(selected, sq, promotion=promotion)
                    if move in board.legal_moves:
                        board.push(move)
                        last_move = move
                        move_count += 1
                        selected = None; legal_sqrs = []
                    else:
                        # Maybe selecting a different piece
                        piece2 = board.piece_at(sq)
                        if piece2 and piece2.color == board.turn:
                            selected = sq
                            legal_sqrs = [m.to_square for m in board.legal_moves
                                          if m.from_square == sq]
                        else:
                            selected = None; legal_sqrs = []

    pygame.quit()


if __name__ == "__main__":
    main()